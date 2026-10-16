#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the full book PDF for project `ai-era-human-learning`.

Source of truth: the effective *versioned* Markdown files (Introduction,
13 chapters, Conclusion). Chapter 04 uses the repair-01 Markdown.

Pipeline:
  1. Parse each Markdown (strip YAML frontmatter, split H1 = chapter title,
     demote remaining H/Downs, convert ```mermaid to PDF via mmdc).
  2. Render each unit (chapter / conclusion) to its own PDF with the shared
     LaTeX `book` preamble (xeCJK: Songti SC + Times New Roman).
  3. Render the Introduction to its own PDF *without* page numbers and
     *without* running head (it is a running prose piece between cover/TOC
     and chapters). Even though it physically has 4 pages, the arabic page
     counter starts at Chapter 01.
  4. Generate a typographic cover (扉页) and a TOC using reportlab with
     embedded Songti SC + Times New Roman, then merge:
         cover(1) + TOC(1) + Introduction(4) + Chapter 01..13 + Conclusion
     and inject a structured bookmark outline.
  5. Write a machine-readable build report (JSON) for the assembler report.

Only reads documents/**; only writes into pdf/build/**, pdf/, and the copy
of chapter PDFs into pdf/. Never touches Markdown/branch/evidence/etc.
"""

import json
import os
import re
import subprocess
import sys
import shutil
import hashlib

WS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
PROJ = os.path.join(WS, "idea-projects", "ai-era-human-learning")
PDFDIR = os.path.join(PROJ, "pdf")
BUILD = os.path.join(PDFDIR, "build")
TEXDIR = os.path.join(BUILD, "tex")
MAINDIR = os.path.join(BUILD, "main")
PROBE = os.path.join(BUILD, "_probe")

os.makedirs(TEXDIR, exist_ok=True)
os.makedirs(MAINDIR, exist_ok=True)
os.makedirs(PROBE, exist_ok=True)

# ---- fonts (verified present on this host) -------------------------------
SERIF_V = "/System/Library/Fonts/Supplemental/Songti.ttc"      # idx 6 = Songti SC Regular
SERIF_IDX = 6
KAI_V = "/System/Library/Fonts/Supplemental/Kaiti.ttc"
SERIFTTF = os.path.join(PROBE, "SongtiSC.ttf")                 # extracted single-face ttf


# ---- input manifest ------------------------------------------------------
def versioned(rel):
    return os.path.join(PROJ, rel)


UNITS = [
    # (key, kind, relpath under PROJ)
    ("introduction", "intro", "introduction/versioned/reading-optimization-20261013/introduction.md"),
    ("chapter-01", "chapter", "branches/1-why-humans-still-learn/versioned/reading-optimization-20261013/chapter-01-why-humans-still-learn.md"),
    ("chapter-02", "chapter", "branches/2-functions-of-knowledge/versioned/reading-optimization-20261013/chapter-02-functions-of-knowledge.md"),
    ("chapter-03", "chapter", "branches/3-knowledge-value-and-selection/versioned/reading-optimization-20261013/chapter-03-knowledge-value-and-selection.md"),
    # Chapter 04 uses the repair-01 Markdown version
    ("chapter-04", "chapter", "branches/4-entering-unknown-domains/versioned/reading-optimization-20261013-repair-01/chapter-04-entering-unknown-domains.md"),
    ("chapter-05", "chapter", "branches/5-knowledge-internalization/versioned/reading-optimization-20261013/chapter-05-knowledge-internalization.md"),
    ("chapter-06", "chapter", "branches/6-feynman-method-position/versioned/reading-optimization-20261013/chapter-06-feynman-method-position.md"),
    ("chapter-07", "chapter", "branches/7-validating-understanding/versioned/reading-optimization-20261013/chapter-07-validating-understanding.md"),
    ("chapter-08", "chapter", "branches/8-knowledge-transfer-and-application/versioned/reading-optimization-20261013/chapter-08-knowledge-transfer-and-application.md"),
    ("chapter-09", "chapter", "branches/9-human-ai-learning-collaboration/versioned/reading-optimization-20261013/chapter-09-human-ai-learning-collaboration.md"),
    ("chapter-10", "chapter", "branches/10-validating-machine-generated-knowledge/versioned/reading-optimization-20261013/chapter-10-validating-machine-generated-knowledge.md"),
    ("chapter-11", "chapter", "branches/11-cross-disciplinary-learning/versioned/reading-optimization-20261013/chapter-11-cross-disciplinary-learning.md"),
    ("chapter-12", "chapter", "branches/12-human-agency-and-responsibility/versioned/reading-optimization-20261013/chapter-12-human-agency-and-responsibility.md"),
    ("chapter-13", "chapter", "branches/13-human-ai-robot-future-boundaries/versioned/reading-optimization-20261013/chapter-13-human-ai-robot-future-boundaries.md"),
    ("conclusion", "conclusion", "conclusion/versioned/reading-optimization-20261013/conclusion.md"),
]

COVER = {
    "title": "机器会回答，人必须理解",
    "subtitle": "AI时代的知识内化、独立判断与主体性",
    "author": "赵  毅",
    "studio": "zhaoyi studio 2026",
}
COVER_IMAGE = os.path.join(PROJ, "cover.png")
TITLEPAGE_MD = os.path.join(BUILD, "frontmatter", "titlepage.md")

RUNNING_HEAD = "机器会回答，人必须理解"


# ---- Markdown helpers ----------------------------------------------------
def read_md(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_frontmatter(text):
    if text.startswith("---"):
        m = re.match(r"^---\n.*?\n---\n?", text, flags=re.S)
        if m:
            return text[m.end():]
    return text


def escape_latex(t):
    # minimal, order matters
    repl = [
        ("\\", r"\textbackslash{}"),
        ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"),
        ("{", r"\{"), ("}", r"\}"),
        ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}"),
    ]
    for a, b in repl:
        t = t.replace(a, b)
    return t


def convert_inline(t):
    """Markdown inline -> LaTeX (tables stripped separate)."""
    # placeholder for inline code
    codes = []
    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes)-1}\x00"
    t = re.sub(r"`([^`]+)`", stash, t)
    # links [text](url) -> text (url) but drop local .md links clutter? keep text only for .md links
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: m.group(1) + ("" if m.group(2).endswith(".md") else " (" + m.group(2) + ")"), t)
    # bold/italic (use function replacements to avoid regex-template escapes)
    t = re.sub(r"\*\*([^*]+)\*\*", lambda m: "\x01" + m.group(1) + "\x02", t)
    t = re.sub(r"\*([^*]+)\*", lambda m: "\x03" + m.group(1) + "\x04", t)
    # escape
    t = escape_latex(t)
    # restore markers
    t = t.replace("\x01", r"\textbf{").replace("\x02", "}")
    t = t.replace("\x03", r"\emph{").replace("\x04", "}")
    # preserve a space that sits between two CJK chars (xeCJK would drop it),
    # e.g. the separator in "第一章 为什么人类仍需学习？"
    _p = "(?<=[\u3400-\u9fff\u3000-\u303f\uff00-\uffef])[ \t]+(?=[\u3400-\u9fff\u3000-\u303f\uff00-\uffef])"
    t = re.sub(_p, lambda m: r"\hspace{0.42em}", t)
    # restore code
    def unstash(m):
        return r"\code{" + escape_latex(codes[int(m.group(1))]) + "}"
    t = re.sub("\x00(\\d+)\x00", unstash, t)
    return t


def mask_code(md):
    """Extract fenced code blocks. Returns (text_with_placeholders, ordered_list)."""
    out, codes = [], []
    parts = re.split(r"(?ms)^```.*?^```[ \t]*$", md)
    matches = re.findall(r"(?ms)^```([^\n]*)\n(.*?)^```[ \t]*$", md)
    for seg in parts:
        out.append(seg)
        if len(codes) < len(matches):
            pass
    # simpler: rebuild by replacing each match
    def repl(m):
        info = m.group(1).strip()
        body = m.group(2)
        codes.append((info, body))
        return f"\n\x01CODE{len(codes)-1}\x01\n"
    text = re.sub(r"(?ms)^```([^\n]*)\n(.*?)^```[ \t]*$", repl, md)
    return text, codes


def render_mermaid(body, out_pdf):
    src = out_pdf + ".mmd"
    # a long chain fits the tall A5 page better as a top-to-bottom flow
    body2 = re.sub(r"flowchart\s+LR", "flowchart TB", body, count=1)
    init = "%%{init: {'theme':'base','themeVariables':{'fontSize':'26px'}}}%%\n"
    with open(src, "w", encoding="utf-8") as f:
        f.write(init + body2)
    # --pdfFit crops the PDF to the chart (otherwise it emits a full Letter page)
    cmd = ["mmdc", "-i", src, "-o", out_pdf, "-b", "white", "--pdfFit",
           "-w", "1600", "-H", "2200"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode == 0 and os.path.exists(out_pdf), (r.stderr or "")[-500:]


def convert_md_body(md, key):
    md = strip_frontmatter(md)
    text, codes = mask_code(md)
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)
    first_h1 = True
    while i < n:
        ln = lines[i]
        s = ln.strip()
        # code placeholder
        m = re.match(r"^\x01CODE(\d+)\x01$", s)
        if m:
            idx = int(m.group(1))
            info, body = codes[idx]
            if info.startswith("mermaid"):
                out_pdf = os.path.join(PROBE, f"mermaid-{key}.pdf")
                ok, err = render_mermaid(body, out_pdf)
                if ok:
                    out.append("")
                    out.append(r"\begin{center}\includegraphics[width=0.98\linewidth,height=0.88\textheight,keepaspectratio]{%s}\end{center}" % out_pdf)
                    out.append("")
                else:
                    sys.stderr.write(f"[warn] mermaid failed for {key}: {err}\n")
                    out.append(r"\begin{quote}\small\ttfamily [图表：mermaid 渲染失败，见源 Markdown]\\end{quote}")
                    out.append("")
            else:
                # text / plain fenced -> verbatim-ish quote
                out.append(r"\begin{quote}\small\code{")
                for bl in body.rstrip("\n").split("\n"):
                    out.append(escape_latex(bl) + r"\\")
                out.append(r"}")
                out.append(r"\end{quote}")
            i += 1
            continue
        # table
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|?\s*$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            ncol = len(header)
            # Use tabularx so the complete table is constrained to the text
            # width; the former fixed 0.44\linewidth per column overflowed
            # as soon as a table had three columns.
            colspec = "|" + "|".join(["Y"] * ncol) + "|"
            out.append(r"\begin{center}\begingroup\fontsize{9.5}{12}\selectfont\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.2}\begin{tabularx}{0.98\linewidth}{%s}\hline" % colspec)
            out.append(" & ".join("\\bfseries " + convert_inline(h) for h in header) + r" \\ \hline")
            for r_ in rows:
                r_ = (r_ + [""] * ncol)[:ncol]
                out.append(" & ".join(convert_inline(c) for c in r_) + r" \\ \hline")
            out.append(r"\end{tabularx}\endgroup\end{center}")
            continue
        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            title = protect_heading_spaces(convert_inline(m.group(2).strip()))
            if lvl == 1 and first_h1:
                first_h1 = False
                out.append(r"\bookheading{%s}" % title)
            elif lvl == 1:
                out.append(r"\section*{%s}" % title)
            elif lvl == 2:
                out.append(r"\bookheadingtwo{%s}" % title)
            elif lvl == 3:
                out.append(r"\bookheadingthree{%s}" % title)
            else:
                out.append(r"\bookheadingthree{%s}" % title)
            i += 1
            continue
        # horizontal rule
        if re.match(r"^-{3,}\s*$", s) or re.match(r"^\*{3,}\s*$", s):
            i += 1
            continue
        # list item
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", ln)
        if m:
            out.append(r"\par\noindent\hangindent=1.6em " + convert_inline(m.group(3)))
            i += 1
            continue
        # blank
        if s == "":
            out.append("")
            i += 1
            continue
        out.append(convert_inline(s))
        i += 1
    # collapse >1 blank lines
    res, blank = [], 0
    for l in out:
        if l.strip() == "":
            blank += 1
            if blank <= 1:
                res.append("")
        else:
            blank = 0
            res.append(l)
    return "\n".join(res)


_QUOTE_OPEN = "“「《‘"
_QUOTE_CLOSE = "”」》’"


def protect_heading_spaces(t):
    """Keep spaces that sit inside CJK quotes non-breaking (as U+3000) so a
    heading never splits a quoted phrase such as “我觉得会了”。"""
    out, in_q = [], False
    for ch in t:
        if ch in _QUOTE_OPEN:
            in_q = True
        elif ch in _QUOTE_CLOSE:
            in_q = False
        if ch == " " and in_q:
            out.append("\u3000")
        else:
            out.append(ch)
    return "".join(out)


def restore_heading_spaces(t):
    return t.replace("\u3000", " ")


def get_h1(md):
    """LaTeX-safe H1 (for headings and the TOC)."""
    md2 = strip_frontmatter(md)
    m = re.search(r"^#\s+(.*)$", md2, flags=re.M)
    return protect_heading_spaces(convert_inline(m.group(1).strip())) if m else ""


def get_h1_plain(md):
    """Plain-text H1 (for PDF bookmarks and the report)."""
    md2 = strip_frontmatter(md)
    m = re.search(r"^#\s+(.*)$", md2, flags=re.M)
    if not m:
        return ""
    t = m.group(1).strip()
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    t = re.sub(r"`([^`]+)`", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip()
    return restore_heading_spaces(t.replace("\u3000", " "))


# ---- LaTeX preamble ------------------------------------------------------
def preamble(kind, chaptitle, pstart=1):
    if kind == "intro":
        head = RUNNING_HEAD
        pagecmd = (r"\pagenumbering{arabic}" + chr(10)
                   + r"\setcounter{page}{%d}" % int(pstart) + chr(10)
                   + r"\pagestyle{bookstyle}")
        firststyle = "plain"
    else:
        head = RUNNING_HEAD
        pagecmd = (r"\pagenumbering{arabic}" + chr(10)
                   + r"\setcounter{page}{%d}" % int(pstart) + chr(10)
                   + r"\pagestyle{bookstyle}")
        firststyle = "plain"
    tpl = r"""
\documentclass[12pt,a5paper,twoside,openany]{book}
\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage[a5paper,top=18mm,bottom=20mm,inner=19mm,outer=15mm,footskip=9mm]{geometry}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{array}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{ragged2e}
\usepackage{fancyhdr}
\usepackage[hidelinks,unicode]{hyperref}

\setCJKmainfont[Path=__DIR__/,BoldFont=SongtiSC-Bold.ttf]{SongtiSC.ttf}
\setCJKsansfont[Path=__DIR__/]{SongtiSC.ttf}
\setCJKmonofont[Path=__DIR__/]{SongtiSC.ttf}
\newCJKfontfamily\heiti[Path=__DIR__/,BoldFont=SongtiSC-Bold.ttf]{SongtiSC.ttf}
\setmainfont{Times New Roman}
\setsansfont{Helvetica Neue}
\setmonofont{Menlo}[Scale=0.82]
\newcommand{\code}[1]{\begingroup\fontsize{9.5}{11}\selectfont\texttt{#1}\endgroup}
\xeCJKsetup{AutoFakeBold=true}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip=0pt plus 1pt
\linespread{1.42}
\setlength{\parindent}{2em}
\setlength{\parskip}{0.5em plus 0.1em}

\def\bookfirststyle{__FIRSTSTYLE__}
\newcommand{\bookheading}[1]{\clearpage\thispagestyle{\bookfirststyle}%
  \vspace*{0.06\textheight}%
  {\centering\begin{minipage}{0.72\textwidth}\centering\heiti\bfseries\fontsize{16.5}{23}\selectfont #1\par\end{minipage}\par}\vspace{1.2em}}
\newcommand{\bookheadingtwo}[1]{\par\vspace{0.7em}{\heiti\bfseries\fontsize{14}{19}\selectfont #1\par}\vspace{0.25em}}
\newcommand{\bookheadingthree}[1]{\par\vspace{0.45em}{\heiti\fontsize{12.5}{17}\selectfont #1\par}\vspace{0.12em}}

\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}

\fancypagestyle{bookstyle}{%
  \fancyhf{}%
  \fancyhead[RO]{\small\heiti __HEAD__}%
  \fancyhead[LE]{\small\heiti __HEAD__}%
  \fancyfoot[C]{\small\thepage}%
  \renewcommand{\headrulewidth}{0.3pt}%
  \renewcommand{\footrulewidth}{0pt}%
}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{-1}
\hypersetup{pdftitle={机器会回答，人必须理解},pdfauthor={赵  毅}}
__PAGECMD__
\begin{document}
"""
    return (tpl.replace("__DIR__", PROBE)
               .replace("__HEAD__", head).replace("__FIRSTSTYLE__", firststyle)
               .replace("__PAGECMD__", pagecmd))


_HTML_RE = __import__("re")


def tex_escape_html(s):
    import html as _html
    for a, b in [("&", "&"), ("<", "<"), (">", ">")]:
        s = s.replace(a, b)
    return s


def make_alt_cover(out_pdf):
    """Fallback cover rendered with xelatex (fully font-controlled)."""
    # balanced two-line main title: break at the fullwidth comma
    if "，" in COVER["title"]:
        head, tail = COVER["title"].split("，", 1)
        t = tex_escape_html(head + "，") + r"\par " + tex_escape_html(tail)
    else:
        t = tex_escape_html(COVER["title"])
    su = tex_escape_html(COVER["subtitle"])
    au = tex_escape_html(COVER["author"])
    st = tex_escape_html(COVER["studio"])
    tex = r"""\documentclass[12pt,a5paper]{article}
\usepackage[a5paper,margin=0pt]{geometry}
\usepackage{fontspec}
\usepackage{xeCJK}
\setCJKmainfont[Path=__DIR__/,BoldFont=SongtiSC-Bold.ttf]{SongtiSC.ttf}
\setmainfont{Times New Roman}
\xeCJKsetup{AutoFakeBold=true}
\pagestyle{empty}
\begin{document}
\vspace*{0.28\textheight}
\begin{center}
{\bfseries\fontsize{26}{34}\selectfont __T__\par}
\vspace{0.55em}
{\fontsize{15}{21}\selectfont\color[HTML]{333333} __SU__\par}
\end{center}
\vfill
\begin{center}{\fontsize{13.5}{19}\selectfont __AU__\par}\end{center}
\vspace*{0.15\textheight}
\begin{center}{\fontsize{10}{14}\selectfont\color[HTML]{737373} __ST__\par}\end{center}
\vspace*{0.05\textheight}
\end{document}
"""
    tex = (tex.replace("__DIR__", PROBE).replace("__T__", t).replace("__SU__", su)
              .replace("__AU__", au).replace("__ST__", st))
    tex_path = os.path.join(TEXDIR, "_cover.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex)
    r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", MAINDIR, tex_path],
                       capture_output=True, text=True, cwd=TEXDIR)
    prod = os.path.join(MAINDIR, "_cover.pdf")
    if r.returncode == 0 and os.path.exists(prod):
        shutil.copyfile(prod, out_pdf)
        return True
    return False


ALT_ENTRIES = None  # set by main() for the xelatex TOC pass


def toc_title_tex(title):
    """将目录标题中“章”和标题之间的普通空格显式保留。"""
    p = r"(?<=[\u3400-\u9fff\u3000-\u303f\uff00-\uffef])[ \t]+(?=[\u3400-\u9fff\u3000-\u303f\uff00-\uffef])"
    return re.sub(p, r"\\hspace{0.42em}", title)


def make_alt_toc(out_pdf, entries):
    rows = []
    for title, page in entries:
        rows.append(r"{\fontsize{10.5}{15}\selectfont %s}\dotfill {\fontsize{10.5}{15}\selectfont %d}\par\vspace{0.32em}"
                    % (toc_title_tex(title), page))
    body = chr(10).join(rows)
    tex = r"""\documentclass[12pt,a5paper]{article}
\usepackage[a5paper,top=18mm,bottom=18mm,left=16mm,right=16mm]{geometry}
\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{xcolor}
\usepackage{setspace}
\setCJKmainfont[Path=__DIR__/,BoldFont=SongtiSC-Bold.ttf]{SongtiSC.ttf}
\setmainfont{Times New Roman}
\xeCJKsetup{AutoFakeBold=true}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\renewcommand{\arraystretch}{1.0}
\begin{document}
\begin{center}{\bfseries\fontsize{18}{24}\selectfont 目录}\end{center}
\vspace{1.0em}
__ROWS__

\end{document}
"""
    tex = tex.replace("__DIR__", PROBE).replace("__ROWS__", body)
    tex_path = os.path.join(TEXDIR, "_toc.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex)
    r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", MAINDIR, tex_path],
                       capture_output=True, text=True, cwd=TEXDIR)
    prod = os.path.join(MAINDIR, "_toc.pdf")
    if r.returncode == 0 and os.path.exists(prod):
        shutil.copyfile(prod, out_pdf)
        return True
    sys.stderr.write("[warn] xelatex TOC failed\n" + (r.stdout or "")[-1500:] + "\n")
    return False


def build_unit(key, kind, relpath, title, pstart=1):
    md = read_md(versioned(relpath))
    body = convert_md_body(md, key)
    tex = preamble(kind, title, pstart) + "\n" + body + "\n\\end{document}\n"
    tex_path = os.path.join(TEXDIR, f"{key}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex)
    r = subprocess.run(
        ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory", MAINDIR, tex_path],
        capture_output=True, text=True, cwd=TEXDIR,
    )
    out_pdf = os.path.join(MAINDIR, f"{key}.pdf")
    ok = r.returncode == 0 and os.path.exists(out_pdf)
    if not ok:
        log = (r.stdout or "")[-2500:]
        sys.stderr.write(f"[error] xelatex failed for {key}\n{log}\n")
    return ok, out_pdf, title


# ---- TOC / cover via reportlab ------------------------------------------
SERIFTTF_B = os.path.join(PROBE, "SongtiSC-Bold.ttf")


def extract_songti_ttf():
    from fontTools.ttLib import TTCollection
    c = TTCollection(SERIF_V)
    c.fonts[SERIF_IDX].save(SERIFTTF)   # Songti SC Regular
    c.fonts[1].save(SERIFTTF_B)         # Songti SC Bold
    c.close()
    return SERIFTTF


TNR = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
TNRB = "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"
TNR_I = "/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf"


def reg_fonts():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont("SongtiSC", SERIFTTF))
    pdfmetrics.registerFont(TTFont("TNR", TNR))
    pdfmetrics.registerFont(TTFont("TNR-Bold", TNRB))
    pdfmetrics.registerFont(TTFont("TNR-Italic", TNR_I))


def w_cjk(s, size):
    from reportlab.pdfbase import pdfmetrics
    return pdfmetrics.stringWidth(s, "SongtiSC", size)


def w_lat(s, size):
    from reportlab.pdfbase import pdfmetrics
    return pdfmetrics.stringWidth(s, "TNR", size)


def draw_center(c, y, text, size, font="SongtiSC", leading=None):
    from reportlab.lib.pagesizes import A5
    c.setFont(font, size)
    c.drawCentredString(A5[0] / 2.0, y, text)


def make_cover(out_pdf):
    """Use cover.png as a full-bleed background; add only missing studio text.

    The image already contains the title, subtitle, author, and divider, so
    re-rendering those strings would create duplicate cover typography.
    cover.png is 2:3 while A5 is 148:210 (slightly wider), therefore the
    image is scaled to page width and cropped vertically, preserving aspect.
    """
    from reportlab.lib.pagesizes import A5
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas
    from PIL import Image
    W, H = A5
    with Image.open(COVER_IMAGE) as im:
        iw, ih = im.size
    scale = W / iw
    draw_w, draw_h = W, ih * scale
    crop_y = (draw_h - H) / 2.0
    c = canvas.Canvas(out_pdf, pagesize=A5)
    c.setTitle(COVER["title"])
    c.setAuthor(COVER["author"])
    c.drawImage(ImageReader(COVER_IMAGE), 0, -crop_y, width=draw_w, height=draw_h,
                preserveAspectRatio=True, mask="auto")
    # The supplied artwork contains all other cover copy, but not the studio.
    c.setFont("TNR", 9.5)
    c.setFillColorRGB(0.94, 0.94, 0.94)
    c.drawCentredString(W / 2, 16 * 2.8346, COVER["studio"])
    c.showPage()
    c.save()


def parse_titlepage_md(path):
    """Read the monochrome title page copy from a tiny frontmatter Markdown.

    Returns (title, subtitle, author, studio). This file is a build input
    only and is never one of the book's source documents.
    """
    text = strip_frontmatter(read_md(path))
    title = subtitle = author = studio = ""
    extra = []
    for ln in text.split("\n"):
        s = ln.strip()
        if not s:
            continue
        m = re.match(r"^#\s+(.*)$", s)
        if m and not title:
            title = m.group(1).strip()
            continue
        m = re.match(r"^>\s*(.*)$", s)
        if m and not subtitle:
            subtitle = m.group(1).strip()
            continue
        extra.append(s)
    if extra:
        author = extra[0]
    if len(extra) >= 2:
        studio = extra[1]
    return title, subtitle, author, studio


def make_titlepage(out_pdf):
    """Monochrome (black-on-white) title page (扉页) parsed from Markdown.

    Kept grayscale so the printed half-title stays clean and clearly distinct
    from the colour cover; fits an A5 page with no bleed.
    """
    from reportlab.lib.pagesizes import A5
    from reportlab.pdfgen import canvas
    W, H = A5
    title, subtitle, author, studio = parse_titlepage_md(TITLEPAGE_MD)
    c = canvas.Canvas(out_pdf, pagesize=A5)
    c.setTitle(title or COVER["title"])
    c.setAuthor(author or COVER["author"])
    # balanced two-line main title, broken at the fullwidth comma
    lines = [title]
    if "，" in title:
        head, tail = title.split("，", 1)
        lines = [head + "，", tail]
    c.setFillColorRGB(0.0, 0.0, 0.0)
    y = H * 0.62
    for ln in lines:
        c.setFont("SongtiSC", 24)
        c.drawCentredString(W / 2, y, ln)
        y -= 32
    y -= 6
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(0.6)
    c.line(W * 0.24, y, W * 0.76, y)
    y -= 26
    if subtitle:
        c.setFont("SongtiSC", 13.5)
        c.drawCentredString(W / 2, y, subtitle)
    if author:
        c.setFont("SongtiSC", 13)
        c.drawCentredString(W / 2, H * 0.30, author)
    if studio:
        c.setFont("TNR", 10)
        c.setFillColorRGB(0.25, 0.25, 0.25)
        c.drawCentredString(W / 2, H * 0.16, studio)
    c.showPage()
    c.save()


def make_toc(out_pdf, entries):
    """entries: list of (title, page)."""
    from reportlab.lib.pagesizes import A5
    from reportlab.pdfgen import canvas
    W, H = A5
    c = canvas.Canvas(out_pdf, pagesize=A5)
    c.setTitle("目录")
    c.setFont("SongtiSC", 18)
    c.drawCentredString(W / 2, H - 30 * 1, "目录")
    y = H - 62
    dots_color = (0.55, 0.55, 0.58)
    for title, page in entries:
        size = 10.5
        c.setFont("SongtiSC", size)
        c.setFillColorRGB(0.1, 0.1, 0.12)
        x = 16 * 2.8346  # ~16mm
        c.drawString(x, y, title)
        tw = w_cjk(title, size)
        pw = w_lat(str(page), size)
        right = W - x
        # dot leaders
        c.setFillColorRGB(*dots_color)
        dot_start = x + tw + 4
        dot_end = right - pw - 4
        if dot_end > dot_start:
            c.setFont("TNR", size)
            d = ". "
            dw = c.stringWidth(d, "TNR", size)
            nd = int((dot_end - dot_start) / dw)
            c.drawString(dot_start, y, d * max(0, nd))
        c.setFont("TNR", size)
        c.setFillColorRGB(0.1, 0.1, 0.12)
        c.drawRightString(right, y, str(page))
        y -= 20
    # note
    c.setFont("SongtiSC", 8.5)
    c.setFillColorRGB(0.5, 0.5, 0.52)
    c.drawString(16 * 2.8346, 30, "说明：目录页码为正文页码；封面、扉页与目录不编号，正文自引言起编阿拉伯页码。")
    c.showPage()
    c.save()


# ---- assembly ------------------------------------------------------------
def main():
    import fitz
    _mds = {key: read_md(versioned(rel)) for key, kind, rel in UNITS}
    titles = {key: get_h1(_mds[key]) for key in _mds}           # LaTeX form
    titles_plain = {key: get_h1_plain(_mds[key]) for key in _mds}  # plain text

    # ---- frontmatter assets ----
    extract_songti_ttf()
    reg_fonts()
    if not os.path.exists(COVER_IMAGE):
        raise FileNotFoundError(f"missing cover image: {COVER_IMAGE}")
    if not os.path.exists(TITLEPAGE_MD):
        raise FileNotFoundError(f"missing titlepage md: {TITLEPAGE_MD}")
    data_mode = "cover-png + titlepage-md(bw) + latex-toc"

    # ---- pass 1: build intro + chapters, derive printed offsets ----
    def build_all(offsets):
        res = []
        for key, kind, rel in UNITS:
            ps = offsets.get(key, 1)
            ok, pdf, title = build_unit(key, kind, rel, titles[key], ps)
            if not ok:
                print(json.dumps({"status": "failed", "unit": key}))
                sys.exit(1)
            d = fitz.open(pdf)
            res.append({"key": key, "kind": kind, "md": rel, "title": titles[key],
                        "pdf": pdf, "pages": d.page_count})
            d.close()
        return res

    # Front matter: cover (1) + monochrome title page (2) + TOC (3); none of
    # these front-matter pages are numbered. The body is renumbered from 1:
    # the Introduction is body page 1, Chapter 01 is body page 11, and so on.
    # Each content unit is written with its correct first body number so the
    # footer folio equals the body index printed in the TOC.
    results = build_all({"introduction": 1})
    intro = next(r for r in results if r["kind"] == "intro")
    chapters = [r for r in results if r["kind"] != "intro"]
    offsets, cum = {"introduction": 1}, 1 + intro["pages"]
    for r in chapters:
        offsets[r["key"]] = cum
        cum += r["pages"]
    printed_total = cum - 1
    # pass 2: rebuild with continuous body-page numbering
    results = build_all(offsets)
    intro = next(r for r in results if r["kind"] == "intro")
    chapters = [r for r in results if r["kind"] != "intro"]
    # TOC and footer share the same body-page numbering.
    toc_entries = [{"title": titles_plain["introduction"], "page": 1, "is_frontmatter": True}]
    toc_entries += [{"title": titles_plain[r["key"]], "page": offsets[r["key"]], "is_frontmatter": False}
                    for r in chapters]

    # ---- cover + title page + toc ----
    cover_pdf = os.path.join(PDFDIR, "frontmatter-cover.pdf")
    titlepage_pdf = os.path.join(PDFDIR, "frontmatter-titlepage.pdf")
    toc_pdf = os.path.join(PDFDIR, "frontmatter-toc.pdf")
    make_cover(cover_pdf)
    make_titlepage(titlepage_pdf)
    make_alt_toc(toc_pdf, [(e["title"], e["page"]) for e in toc_entries])

    # ---- merge ----
    out = os.path.join(PDFDIR, "ai-era-human-learning-book.pdf")
    doc = fitz.open()
    doc.insert_pdf(fitz.open(cover_pdf))
    doc.insert_pdf(fitz.open(titlepage_pdf))
    doc.insert_pdf(fitz.open(toc_pdf))
    doc.insert_pdf(fitz.open(intro["pdf"]))
    for r in chapters:
        doc.insert_pdf(fitz.open(r["pdf"]))

    # bookmarks (1-based physical pages) — distinct from the body folio:
    # cover(1)/titlepage(2)/TOC(3), Introduction starts at physical page 4.
    phys = 4 + intro["pages"]  # physical page of chapter 01
    toc = [[1, "封面", 1], [1, "扉页", 2], [1, "目录", 3],
           [1, titles_plain["introduction"], 4]]
    for r in chapters:
        toc.append([1, titles_plain[r["key"]], phys])
        phys += r["pages"]
    doc.set_toc(toc)

    doc.set_metadata({
        "title": "机器会回答，人必须理解",
        "author": "赵  毅",
        "subject": "AI时代的知识内化、独立判断与主体性",
        "creator": "xelatex(book) + frontmatter build_book.py",
    })
    doc.save(out, garbage=4, deflate=True)
    n = doc.page_count
    doc.close()

    # 5. copy per-chapter pdfs into pdf/ (update mapped names)
    mapping = {
        "introduction": "chapter-00-introduction.pdf",
        "chapter-01": "chapter-01-why-humans-still-learn.pdf",
        "chapter-02": "chapter-02-functions-of-knowledge.pdf",
        "chapter-03": "chapter-03-knowledge-value-and-selection.pdf",
        "chapter-04": "chapter-04-entering-unknown-domains.pdf",
        "chapter-05": "chapter-05-knowledge-internalization.pdf",
        "chapter-06": "chapter-06-feynman-method-position.pdf",
        "chapter-07": "chapter-07-validating-understanding.pdf",
        "chapter-08": "chapter-08-knowledge-transfer-and-application.pdf",
        "chapter-09": "chapter-09-human-ai-learning-collaboration.pdf",
        "chapter-10": "chapter-10-validating-machine-generated-knowledge.pdf",
        "chapter-11": "chapter-11-cross-disciplinary-learning.pdf",
        "chapter-12": "chapter-12-human-agency-and-responsibility.pdf",
        "chapter-13": "chapter-13-human-ai-robot-future-boundaries.pdf",
        "conclusion": "chapter-14-conclusion.pdf",
    }
    for r in results:
        if r["key"] in mapping:
            shutil.copyfile(r["pdf"], os.path.join(PDFDIR, mapping[r["key"]]))

    report = {
        "status": "success",
        "book": out,
        "pages": n,
        "cover": cover_pdf,
        "cover_image": os.path.relpath(COVER_IMAGE, WS),
        "cover_image_size_px": [1536, 2304],
        "cover_strategy": "scale-to-A5-width; centered vertical crop; preserve aspect ratio; add only missing studio text",
        "titlepage": titlepage_pdf,
        "titlepage_md": os.path.relpath(TITLEPAGE_MD, WS),
        "titlepage_style": "monochrome black-on-white; parsed from Markdown frontmatter",
        "toc": toc_pdf,
        "bookmarks": toc,
        "toc_entries": toc_entries,
        "offsets": offsets,
        "units": [dict(u, title=titles_plain[u["key"]]) for u in results],
        "printed_total": printed_total,
        "intro_pages": intro["pages"],
        "data_mode": data_mode,
        "source_markdown_recompiled": True,
        "source_markdown_modified": False,
    }
    with open(os.path.join(BUILD, "build_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps({"status": "success", "book": out, "pages": n,
                      "printed_total": printed_total}))


if __name__ == "__main__":
    main()
