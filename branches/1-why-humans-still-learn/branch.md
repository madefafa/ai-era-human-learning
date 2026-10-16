---
project_id: "ai-era-human-learning"
branch_id: "why-humans-still-learn"
branch_number: 1
name: "为什么人类仍需学习"
status: draft
question: "AI 能替代哪些学习，不能替代哪些学习？"
objective: "形成文章开篇的主论证，提出‘学习不会消失，但学习对象发生变化’的限定性结论"
priority: "P0"
domain: general
constraints:
  - "区分事实、用户观点、模型推论、未来情景和未知事项"
  - "不把 AI 超越人类、超级智能或技术终局写成已证实事实"
  - "不把检索、生成或流畅表达直接等同于理解"
  - "不预设人类学习价值已经被某一种未来技术结论决定"
assumptions:
  - "AI 可能降低部分记忆、检索和表达任务的必要性，但该判断需要具体分析"
  - "学习可能仍与概念模型、问题意识、判断、责任和价值选择有关"
  - "如果 AI 在所有任务上都比人类更可靠，人类学习是否仍有独立价值，是必须保留的反方问题"
created_at: "2026-10-11T14:14:07+08:00"
updated_at: "2026-10-11T23:48:00+08:00"
initial_operation_id: "op-ai-learning-20261011-06"
last_operation_id: "op-ai-learning-chapter-20261011-01"
search_status: "not-started"
---

# 用户输入

- 用户同意 13 个 issues 的安排，并要求先将 issues 落盘，再处理第一个 branch。
- 用户授权：`授权创建 branch op-ai-learning-20261011-06`。
- 本 branch 对应 outline 中的 Issue 1：`why-humans-still-learn`。

# 已确认内容

- 本 branch 是项目的第一个正式一级 branch，`branch_number: 1`。
- 目标读者为普通读者；项目用途为思想/科普长文。
- 本 branch 先处理学习的必要性，再连接后续的知识功能、知识内化和人机协同议题。
- 研究范围包括记忆性学习、概念模型、问题意识、判断、责任和价值选择的关系。
- 需要保留反方问题：如果 AI 在所有任务上都比人类更可靠，人类学习是否仍有独立价值？

# 待确认问题

- “学习”在本 branch 中是指哪些活动：事实记忆、概念理解、技能练习、价值形成、社会化实践，还是以上层次的组合？
- “替代”按什么标准判断：速度、准确率、成本、责任承担、迁移能力、主体体验，还是综合标准？
- 文章的主论证应主要依赖现实中的 AI 使用经验、学习科学材料、哲学论证，还是三者结合？
- 哪些学习内容即使可以由 AI 随时提供，也仍应保留在人的长期记忆或身体技能中？

# 模型推论

以下内容是待论证的工作假设，不是已确认事实：

- AI 可能改变学习的重点，但“改变重点”不自动等于“人类不再需要学习”。
- 外部工具可以提供答案，但答案的选择、解释、验证、迁移和后果承担可能仍需要人的能力；具体边界待研究。
- 学习的价值可能不仅在于储存信息，还在于塑造观察、提问、判断和行动的能力；该命题需要区分经验性主张和价值判断。

# 检索记录

## 20261011-ai-learning-01

- operation_id: `op-ai-learning-search-20261011-01`
- status: `completed`
- executed_at: `2026-10-11T14:28:13+08:00`
- queries:
  - `learning science retrieval practice transfer metacognition durable understanding`
  - `AI assisted learning human judgment critical thinking cognitive offloading`
  - `expertise background knowledge problem solving learning`
  - `AI education human agency responsibility decision making`
- itemnums: `15 per query`
- categories: `science,general`
- result: `4/4 success; returned candidate scales 224, 155, 279, 293; retry_count=0`
- record: `searches/20261011-ai-learning-01.md`
- evidence_state: `10 candidate cards committed; snippets not treated as final evidence`

# 证据索引

| evidence_id | 主张/用途 | 来源类型 | 支持关系 | 置信度 | 路径 |
|---|---|---|---|---|---|
| carpenter-effective-learning-20261011 | 间隔、主动提取和元认知可能支持持久学习 | paper | supports | medium | `evidence/carpenter-effective-learning-20261011.md` |
| retrieval-based-learning-20261011 | 主动提取可能比被动重读更有利于有意义学习 | paper | supports | medium | `evidence/retrieval-based-learning-20261011.md` |
| national-academies-expertise-20261011 | 浅层覆盖可能不足以形成未来学习/工作能力 | official | supports | medium | `evidence/national-academies-expertise-20261011.md` |
| frontiers-problem-solving-expertise-20261011 | 示例、练习与问题结构可能参与问题解决能力形成 | paper | contextual | low | `evidence/frontiers-problem-solving-expertise-20261011.md` |
| pmc-cognitive-paradox-ai-education-20261011 | AI 可能同时增强信息处理并带来高阶判断风险 | paper | contextual | low | `evidence/pmc-cognitive-paradox-ai-education-20261011.md` |
| mdpi-cognitive-offloading-20261011 | 认知外包与批判性思维之间存在待核验风险 | paper | contextual | low | `evidence/mdpi-cognitive-offloading-20261011.md` |
| apa-ai-human-skills-20261011 | AI 可能扩大批判性思维、判断和创造任务的外包 | official | contextual | low | `evidence/apa-ai-human-skills-20261011.md` |
| bera-human-ai-agency-20261011 | 教育主体性可通过可追踪的人机互动行为分析 | paper | contextual | low | `evidence/bera-human-ai-agency-20261011.md` |
| openpraxis-human-agency-authority-20261011 | 生成式 AI 可能改变知识生产与评价的权威关系 | paper | contextual | low | `evidence/openpraxis-human-agency-authority-20261011.md` |
| deloitte-ai-decision-accountability-20261011 | AI 决策中的问责需要人类主体性和责任链条 | official | contextual | low | `evidence/deloitte-ai-decision-accountability-20261011.md` |

# Branch 询问记录

## ASK-20261011-0001：Issue 1 branch 创建

- operation_id: `op-ai-learning-20261011-06`
- time: `2026-10-11T14:14:07+08:00`
- user_question: `我想就 outline 中的 learning-and-internalization 进行聚焦扩展论述，并同意 13 个 issue 的安排；先落盘 issues，再处理第一个 branch`
- analysis: `将 Issue 1 独立为 why-humans-still-learn，作为文章主论证的入口；不预先断言 AI 或超级智能的技术终局`
- status: `committed`

# Summary 索引

| summary_id | status | 生成操作 | 路径 |
|---|---|---|---|
| `20261011-why-humans-still-learn-draft-01` | draft / awaiting-confirmation | `op-ai-learning-draft-20261011-01` | `summaries/20261011-why-humans-still-learn-draft-01.md` |
| `20261011-why-humans-still-learn-chapter-01-draft` | draft / awaiting-confirmation | `op-ai-learning-chapter-20261011-01` | `summaries/20261011-why-humans-still-learn-chapter-01-draft.md` |

该 draft 基于一次 webgo batch 和 10 张候选证据卡；尚未逐篇全文核验，不构成最终结论。

章节 draft `20261011-why-humans-still-learn-chapter-01-draft` 基于上述 draft、10 张候选证据卡与本 branch 本地数字资产编写，风格为学术科普风；未新调用 webgo，未执行全文核验，未标记 confirmed。

# 未解决事项

- “学习”与“替代”的操作性标准仍未完全定义。
- 尚未逐篇打开候选来源全文，核对样本、方法、发表状态、效应量和引用上下文。
- 当前较强相关材料主要支持主动提取、学习策略和背景知识的候选机制；AI 对学习的实际因果影响仍证据不足。
- AI 认知外包、批判性思维、主体性和责任相关材料目前多为搜索摘要级上下文，不能直接升级为确定事实。
- 尚未区分哪些学习功能可以外包给 AI，哪些功能需要人保留；需要按任务类型、学习者水平和风险分析。
- 尚未充分处理“如果 AI 在所有任务上都比人类更可靠，人类学习是否仍有独立价值”的反方情景。
- 尚未决定是否需要对高影响主张进行第二轮定向全文核验；如需检索，必须另行授权。
- 第一章 draft 仅完成结构层面的反方情景处理（标注为未来情景/规范性思想实验），尚未转化为可核验材料。
- 第一章与 Issue 2「知识的功能」、Issue 5「知识内化的机制」的衔接尚未完成，存在重复讨论风险。

# 操作日志

## EVT-20261011-branch-0001

- operation_id: `op-ai-learning-20261011-06`
- event_type: `branch-create`
- occurred_at: `2026-10-11T14:14:07+08:00`
- recorded_at: `2026-10-11T14:14:40+08:00`
- actor: `user + idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-05`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/1-why-humans-still-learn/branch.md`
  - `idea-projects/ai-era-human-learning/branches/1-why-humans-still-learn/searches/`
  - `idea-projects/ai-era-human-learning/branches/1-why-humans-still-learn/evidence/`
  - `idea-projects/ai-era-human-learning/branches/1-why-humans-still-learn/summaries/`
- user_authorization: `授权创建 branch op-ai-learning-20261011-06`
- before: `候选仅存在于 branches/outline.md；正式 branch 数量为 0`
- after: `正式 branch 1 已创建，状态 draft；current_branch 未切换，仍为 null`
- not_executed: `未调用 webgo；未创建 evidence 或 summary`

## EVT-20261011-branch-0002：切换为当前 branch

- operation_id: `op-ai-learning-20261011-07`
- event_type: `branch-switch`
- occurred_at: `2026-10-11T14:22:57+08:00`
- recorded_at: `2026-10-11T14:23:32+08:00`
- actor: `user + idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-06`
- before: `current_branch=null`
- after: `current_branch=why-humans-still-learn`
- user_decision: `切换到 branch why-humans-still-learn，并继续生成 webgo 检索计划`
- impact: `后续 ask/search/summary 默认作用于本 branch`
- not_executed: `尚未执行 webgo；检索授权仍待单独确认`

## EVT-20261011-branch-0003：webgo 检索与证据落盘

- operation_id: `op-ai-learning-search-20261011-01`
- event_type: `search`
- occurred_at: `2026-10-11T14:26:48+08:00`
- recorded_at: `2026-10-11T14:40:45+08:00`
- actor: `user + idea-navigator + webgo`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-07`
- affected_paths:
  - `searches/20261011-ai-learning-01.md`
  - `evidence/`
  - `branch.md`
- authorization: `确认执行检索 op-ai-learning-search-20261011-01`
- parameters: `4 queries; itemnums=15 per query; categories=science,general`
- result: `4/4 successful; no failed queries; substantial noise retained in audit record`
- persistence: `search record and 10 candidate evidence cards committed`
- limitations: `snippets were not treated as final evidence; full-text verification pending`

## EVT-20261011-branch-0004：生成 Issue 1 draft

- operation_id: `op-ai-learning-draft-20261011-01`
- event_type: `summary`
- occurred_at: `2026-10-11T14:45:30+08:00`
- recorded_at: `2026-10-11T14:48:10+08:00`
- actor: `idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-search-20261011-01`
- affected_paths:
  - `summaries/20261011-why-humans-still-learn-draft-01.md`
  - `branch.md`
- purpose: `基于检索候选和证据边界形成 Issue 1 的探索性 draft`
- summary_status: `draft / awaiting-confirmation`
- evidence_basis: `10 candidate cards; search snippets; full-text verification pending`
- main_claim: `AI 可能降低部分记忆、检索和表达任务的成本，但不等于人类不再需要学习；学习重点可能转向理解、判断、迁移和责任`
- not_executed: `未将 summary 标记为 confirmed；未宣称候选证据已完成全文核验`

## EVT-20261011-branch-0005：生成 Issue 1 学术科普风第一章 draft

- operation_id: `op-ai-learning-chapter-20261011-01`
- event_type: `summary`
- occurred_at: `2026-10-11T23:48:00+08:00`
- recorded_at: `2026-10-11T23:48:00+08:00`
- actor: `user + code`
- status: `committed`
- parent_operation_id: `op-ai-learning-pause-20261011-01`
- affected_paths:
  - `summaries/20261011-why-humans-still-learn-chapter-01-draft.md`
  - `branch.md`
- purpose: `利用本 branch 数字资产编写《第一章 为什么人类仍需学习？》，风格为学术科普风`
- summary_status: `draft / awaiting-confirmation`
- evidence_basis: `10 candidate cards; existing draft summary; no new webgo call`
- main_claim: `学习不会消失，但学习对象和重点可能发生变化；AI 降低部分记忆、检索、表达成本，不等于取消学习`
- structure: `引言场景 → 定义学习与替代 → 学习科学材料 → 可外包侧 → 不可仅靠外包侧 → 认知外包双刃剑 → 反方情景 → 限定性结论 → 证据与边界附录`
- not_executed: `未新调用 webgo；未执行全文核验；未将章节标记为 confirmed；未修改其他 branch 或其他 issue`

## EVT-20261011-branch-0006：生成读者交付版第一章正文

- operation_id: `op-ai-learning-chapter-delivery-20261011-01`
- event_type: `update`
- occurred_at: `2026-10-11T23:52:00+08:00`
- recorded_at: `2026-10-11T23:52:00+08:00`
- actor: `user + code`
- status: `committed`
- parent_operation_id: `op-ai-learning-chapter-20261011-01`
- affected_paths:
  - `chapter-01.md`
  - `branch.md`
- purpose: `将研究型 chapter draft 转换为可直接交付读者的独立章节正文`
- delivery_status: `created`
- result: `新增 chapter-01.md；保留原 summaries/ 下研究工作稿不变`
- content_boundary: `正文不含 front matter、研究状态、证据标签、证据卡表格、审计字段和证据附录；保留自然语言限定表达与下一章过渡`
- validation: `217 行；章节标题、八节结构和结尾过渡存在；研究元数据扫描 clean`
- not_executed: `未删除或覆盖研究工作稿；未调用 webgo；未执行全文核验；未修改其他 branch 或 issue`
