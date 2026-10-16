---
project_id: "ai-era-human-learning"
branch_id: "human-ai-learning-collaboration"
branch_number: 9
search_id: "20261012-human-ai-collab-search-01"
operation_id: "op-ai-human-ai-collab-search-20261012-01"
parent_operation_id: "op-ai-learning-20261012-24"
status: completed
retrieved_at: "2026-10-12T07:30:32Z"
itemnums: 15
categories: "science,general"
confirmed: true
---

# Issue 9 检索记录：人与 AI 的学习协同

## 授权与边界

- 用户授权原文：`确认执行检索 op-ai-human-ai-collab-search-20261012-01`。
- 本次严格只作用于 `branches/9-human-ai-learning-collaboration/`；不处理 Issue 10–13，不修改 Issue 1–8，不创建其他 branch，不切换 `current_branch`。
- parent_operation_id：`op-ai-learning-20261012-24`；current_branch 预期并保持 `human-ai-learning-collaboration`。

## 参数与真实返回状态

webgo 使用一次严格四查询 batch；每项均显式传入 `itemnums=15`、`categories=science,general`。

| # | query | status | exit_code | returned_itemnums / item_count | stop_reason | page_count | duplicates_removed | failed engines |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | human AI collaboration learning cognitive offloading division of labor education | success | 0 | 166 / 166 | target_reached | 1 | 4 | 未报告 |
| 2 | AI assisted learning metacognition agency human oversight judgment | success | 0 | 149 / 149 | target_reached | 1 | 0 | 未报告 |
| 3 | generative AI education delegation verification critical thinking | success | 0 | 179 / 179 | target_reached | 1 | 0 | 未报告 |
| 4 | human AI complementary performance task allocation learning | success | 0 | 193 / 193 | target_reached | 1 | 4 | 未报告 |

batch 总体：`exit_code=0`，requested_count=4，completed_count=4，failed_count=0，retry_count=0，success_rate=1.0，failure_rate=0.0，elapsed_seconds=37.4659869169991。返回候选合计 687；该数字不是证据数量。四项均 target_reached 只表示达到工具返回阈值，不表示主题收敛、质量合格或因果证据充分。

## 诊断、失败引擎与噪声

- diagnostics：四项均单页、target_reached；batch 无失败任务、无重试；失败引擎字段未报告。
- 去重：查询 1 和 4 各移除 4 条；查询 2、3 为 0。跨查询语义重复仍需人工判断，不能由该字段推断全局去重完成。
- 噪声：词典/百科与公司页面；LinkedIn、Medium、商业营销页；ResearchGate、arXiv/预印本和摘要级条目；多语言结果；与学习主题弱相关的 transfer、一般 AI 站点、招聘/组织页面；部分结果含未来日期或仅有搜索摘要。以下卡片只保留与 Issue 9 直接相关且可形成明确边界的候选，均未作全文核验。
- 证据边界：检索摘要可以支持“候选主张/研究方向”，不能据此臆测样本、方法、效应量、因果方向或适用人群。

## 候选索引（按四项查询的返回前列登记）

### Query 1

1. [Cognitive offloading in student–AI collaboration: A longitudinal analysis of prompting strategies](https://www.sciencedirect.com/science/article/pii/S2451958826002046) — 认知外包/学生—AI 协同候选
2. [Between Human and Machine: University Teachers’ Accounts of Judgment, Metacognitive Defense, and Cognitive Offloading in Generative AI Use](https://www.mdpi.com/2079-3200/14/10/254) — 判断、元认知防御、认知外包候选
3. [Augmentation or Erosion? Regulating Cognitive Offloading in ...](https://link.springer.com/article/10.1007/s10648-026-10224-6) — 外包的增强/侵蚀条件候选
4. [Human and AI collaboration in the higher education environment](https://pmc.ncbi.nlm.nih.gov/articles/PMC11001814/) — 高等教育人机协同框架候选
5. [Generative AI in Human-AI Collaboration: Validation of ...](https://www.tandfonline.com/doi/full/10.1080/10447318.2025.2543997) — 战略性认知分工候选
6. [From Passive Tool to Socio-cognitive Teammate](https://arxiv.org/html/2508.14825v1) — AI 素养与评价输出候选
7. [AI and cognitive offloading](https://www.ei-ie.org/en/item/32652:ai-and-cognitive-offloading-supporting-teachers-to-shape-ais-impact-on-learning) — 教学设计/努力加工候选
8. [Cognitive reshaping and resurgence of humanness](https://doi.org/10.3389/fmed.2026.1867722) — 医学教育中的认知外包候选
9–15. 其余返回项含韩文数据库、AI 研究中心、LinkedIn、Wikipedia、词典、大学行政页和弱相关公司页面，登记为噪声或待核验，不计证据卡。

### Query 2

1. [(PDF) Human Metacognition in AI-Assisted Decision-Making](https://www.researchgate.net/publication/394305431_Human_Metacognition_in_AI-Assisted_Decision-Making) — 元认知监控候选，来源层级低
2. [Artificial Intelligence Mismatch Between Work and K-12](https://knowledgeworks.org/resources/expertise-paradox-work-k-12-education/) — 判断/监督与学习路径候选
3. [The System 3 Method](https://doi.org/10.3389/fpsyg.2026.1891793) — 学习者 agency/创造性元认知候选
4. [Fostering Human Agency in Age of AI](https://learning-analytics.info/index.php/JLA/article/download/9485/7947/46901) — agency、透明度、教师选择候选
5. [Judgment of Learning: A Human Ability Beyond Generative Artificial Intelligence](https://arxiv.org/abs/2410.13392) — 学习判断与监督候选
6. [Human Oversight as a Dimension of Well-being Efficacy in AI](https://arxiv.org/pdf/2512.13768) — 人类 agency/责任候选
7. [Understanding learners and the interplay between metacognitive judgements of learning and AI-generated explanations](https://deepblue.lib.umich.edu/items/4aac7909-4a47-4e97-982a-f61d318a3013) — 学习判断与 AI 解释候选
8–15. LinkedIn、AI 公司主页、博客、Wiki/Wikibooks 与弱相关平台条目，登记为噪声/待核验。

### Query 3

1. [Generative AI and Critical Thinking in Higher Education](https://www.ojed.org/jise/article/download/10565/3995) — 委托 evaluation/synthesis/verification 候选
2. [What Does the Credential Still Certify? Cognitive ...](https://ojs.aaai.org/index.php/AIES/article/view/43349/50909) — 从完成任务转向验证的候选
3. [Between cognitive offloading and critical autonomy](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1878665/full) — 系统综述/批判自主性候选
4. [Understanding critical thinking in generative artificial intelligence use](https://www.sciencedirect.com/science/article/pii/S2451958826001776) — verification、epistemic motivation、reflective judgement 候选
5. [The role of critical thinking on undergraduates’ reliance behaviours](https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13613) — 依赖行为与批判思维候选
6. [The Impact of Generative AI on Critical Thinking](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf) — 综述/调查候选，需核方法
7. [Verifying generative AI in schools](https://www.uoc.edu/en/news/2026/only-ten-percent-school-students-verify-generative-ai) — 学生核验行为候选，新闻稿层级
8–15. 词典、LinkedIn、arXiv 新预印本、ACM 页面、工程验证博客与无关教育产品页面，登记为噪声/待核验。

### Query 4

1. [Roles of Artificial Intelligence in Collaboration with Humans: Automation, Augmentation, and the Future of Work](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05684) — 任务分配/automation-augmentation 候选
2. [Toward Human-AI Complementarity Across Diverse Tasks](https://arxiv.org/html/2605.04070v1) — 按置信度/任务特征路由候选
3. [Learning Complementary Policies for Human-AI Teams](https://arxiv.org/abs/2302.02944) — 互补策略/分工候选
4. [Analytical Review of Task Allocation Methods for Human and AI](https://journals.rcsi.science/2713-3192/article/view/278228) — 任务分配综述候选
5. [Human-AI Complementarity: A Goal for Amplified Oversight](https://deepmindsafetyresearch.medium.com/human-ai-complementarity-a-goal-for-amplified-oversight-0ad8a44cae0a) — 互补与监督候选，Medium 层级
6. [A Systematic Literature Review on Task Allocation, Communication, Interaction, and Cognitive Augmentation](https://www.sciencedirect.com/science/article/pii/S1877050926003716) — 协同机制候选
7. [A Complementarity-Enhanced Mixture of Human-AI Teams for Decision-Making](https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2025/research/preprint_ecml_pkdd_2025_research_292.pdf) — 互补建模候选，预印本
8. [Collaborative Intelligence: A scoping review of current applications](https://www.qeios.com/read/RZGEPB) — 互补性范围候选
9–15. 词典、Wikipedia、一般人因页面、SDG 页面、韩文数据库和弱相关公司/平台页面，登记为噪声/待核验。

## 用户汇报摘要

- 实际状态：webgo batch `exit_code=0`，4/4 success，0 failed，0 retry；规模为 166、149、179、193（合计 687 候选），不是 687 条证据。
- 主要线索：认知外包可能同时带来效率/增强与分析投入下降风险；元认知、agency、监督和判断是人类学习者保留环节的候选机制；delegation 后的 verification/反思可能是关键控制点；互补性依赖任务特征与路由，而不是固定“AI 做一半、人做一半”。这些是候选线索，不是已核验结论。
- 落盘状态：本检索记录、8 张候选证据卡、1 份 draft、branch/project/decisions/MEMORY 同步均已写入；所有卡片为摘要级候选，未全文核验；draft `confirmed=false`。

## 证据边界与后续

返回规模很大且含明显噪声；当前 8 张卡仅用于建立候选论证骨架。下一步应逐卡打开来源、核对全文、出版状态、研究设计、样本/任务与结果，并处理跨查询重复和可能冲突；不得把搜索摘要升级为事实或因果证据。
