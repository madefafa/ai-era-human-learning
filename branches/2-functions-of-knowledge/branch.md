---
project_id: "ai-era-human-learning"
branch_id: "functions-of-knowledge"
branch_number: 2
name: "知识的功能"
status: draft
question: "知识除了储存事实，还如何影响人的观察、提问、理解和行动？"
objective: "区分信息、知识、理解、能力、判断和智慧，说明背景知识如何构成认知框架、问题空间、判断标准与可能性边界"
priority: "P0"
domain: general
constraints:
  - "区分事实、用户输入、模型推论、待确认问题和未解决事项"
  - "不把知识、理解、能力、判断和智慧预设为同义概念"
  - "不把模型推论或未来情景写成已确认事实"
  - "不执行外部检索，除非另行展示计划并取得单次明确授权"
assumptions:
  - "背景知识可能影响人对信息重要性、相关性和异常性的识别"
  - "知识可能参与构成问题空间、判断标准和行动可能性边界"
  - "信息到知识、理解、能力、判断和智慧之间存在需要区分的转换层次"
created_at: "2026-10-11T14:58:35+08:00"
updated_at: "2026-10-11T15:26:00+08:00"
initial_operation_id: "op-ai-learning-20261011-08"
parent_operation_id: "op-ai-learning-20261011-07"
search_status: completed
last_operation_id: "op-ai-knowledge-functions-draft-20261011-01"
---

# 用户输入

- 用户明确指定本 branch 对应 Issue 2：`functions-of-knowledge`。
- 用户授权原文：`授权创建 branch op-ai-learning-20261011-08`。
- 用户指定名称：`知识的功能`。
- 用户指定问题：`知识除了储存事实，还如何影响人的观察、提问、理解和行动？`。
- 用户指定目标：`区分信息、知识、理解、能力、判断和智慧，说明背景知识如何构成认知框架、问题空间、判断标准与可能性边界。`
- 用户要求只完成 branch 创建，不执行 webgo，不创建 evidence 内容，不生成 summary/draft，不切换 current_branch，不处理 Issue 3–13。

# 已确认内容

- 本 branch 是项目的第二个正式一级 branch，`branch_number: 2`。
- branch_id 为 `functions-of-knowledge`，正式路径为 `branches/2-functions-of-knowledge/branch.md`。
- branch 状态为 `draft`，检索状态为 `not-started`。
- 当前项目的 `current_branch` 已切换为 `functions-of-knowledge`。
- 本次切换未改变 Issue 2 的研究内容、branch 状态或检索状态。

# 待确认问题

- 信息、知识、理解、能力、判断和智慧的操作性边界及相互关系如何定义？
- 背景知识如何影响注意、观察、提问、解释和异常识别？
- 如何区分知识构成的认知框架与知识造成的先入之见或盲点？
- 判断标准来自事实知识、经验、价值承诺和责任要求的比例如何区分？
- “可能性边界”是指可想象、可理解、可验证还是可行动的边界？

# 模型推论

以下内容是待论证的工作假设，不是已确认事实：

- 知识的功能可能不止是储存可调用的事实，还可能改变人对对象的分类、注意分配、问题生成和解释路径。
- 背景知识可能使某些信号变得可见、可命名和可比较，也可能通过既有框架限制对异常或替代解释的注意。
- 信息、知识、理解、能力、判断和智慧可能表现为不同层次：从可获得内容，到结构化关系、机制解释、可靠行动、情境选择与长期后果权衡；具体边界待确认。

# 检索记录

## SEARCH-20261011-01：Issue 2 检索（op-ai-knowledge-functions-search-20261011-01）

- search_id: `20261011-ai-knowledge-functions-search-01`
- operation_id: `op-ai-knowledge-functions-search-20261011-01`
- parent_operation_id: `op-ai-learning-20261011-09`
- status: `completed`
- retrieved_at: `2026-10-11T15:18:48Z`
- queried_at: `2026-10-11T15:18Z`
- itemnums: 15（每项）
- categories: `science,general`
- 查询词：
  1. `background knowledge cognitive schema comprehension problem representation`
  2. `knowledge expertise perception attention reasoning problem solving`
  3. `declarative procedural conceptual knowledge understanding transfer`
  4. `knowledge judgment wisdom decision making education`
- 工具状态：`exit_code=0`；4/4 成功；失败 0；成功率为 1.0；重试 0；耗时约 60.09 秒。
- 返回规模：242、260、226、269（候选返回规模，非证据数）。
- 诊断：四项均 `stop_reason=target_reached`、`page_count=1`；`duplicates_removed` 分别为 0、1、2、0；未报告失败引擎。
- 噪声：包含词典、商业博客、Wikipedia、推广页、个人主页、跨领域与未来日期条目；已保留未静默丢弃。
- 检索记录路径：[`searches/20261011-ai-knowledge-functions-search-01.md`](searches/20261011-ai-knowledge-functions-search-01.md)
- 边界：所有来源仅为候选摘要级，未逐篇核验全文。

后续检索须重新展示脱敏计划并取得绑定新 `operation_id` 的明确授权。

# 证据索引

以下 8 张卡片均基于候选搜索摘要，**未完成全文核验**，只作为方向性候选证据。

| evidence_id | 主张（简写） | 来源标题 | support | confidence | 路径 |
|---|---|---|---|---|---|
| tandf-background-knowledge-comprehension-20261011 | 背景知识参与阅读理解 | The Role of Background Knowledge in Reading Comprehension | supports | medium | [`evidence/tandf-background-knowledge-comprehension-20261011.md`](evidence/tandf-background-knowledge-comprehension-20261011.md) |
| ebsco-schema-theory-20261011 | 图式作为组织新信息的认知框架 | Schema Theory (EBSCO) | contextual | low | [`evidence/ebsco-schema-theory-20261011.md`](evidence/ebsco-schema-theory-20261011.md) |
| pmc-diagnostic-schemas-20261011 | 图式组块化知识以利调用 | Diagnostic Schemas: Form and Function | supports | medium | [`evidence/pmc-diagnostic-schemas-20261011.md`](evidence/pmc-diagnostic-schemas-20261011.md) |
| pmc-human-intelligence-brain-networks-20261011 | 智力与多种认知过程相关 | Human intelligence and brain networks | contextual | low | [`evidence/pmc-human-intelligence-brain-networks-20261011.md`](evidence/pmc-human-intelligence-brain-networks-20261011.md) |
| asu-complex-declarative-learning-20261011 | 陈述性与程序性知识可区分 | Complex Declarative Learning | supports | medium | [`evidence/asu-complex-declarative-learning-20261011.md`](evidence/asu-complex-declarative-learning-20261011.md) |
| wikipedia-procedural-knowledge-20261011 | 概念理解可能与迁移相关 | Procedural knowledge (Wikipedia) | contextual | low | [`evidence/wikipedia-procedural-knowledge-20261011.md`](evidence/wikipedia-procedural-knowledge-20261011.md) |
| mdpi-knowledge-to-wisdom-20261011 | 知识到智慧涉及判断与决策 | From Knowledge to Wisdom (MDPI) | supports | medium | [`evidence/mdpi-knowledge-to-wisdom-20261011.md`](evidence/mdpi-knowledge-to-wisdom-20261011.md) |
| utk-phronesis-practical-wisdom-20261011 | 实践智慧是情境判断 | Practical wisdom relies on human judgment | contextual | low | [`evidence/utk-phronesis-practical-wisdom-20261011.md`](evidence/utk-phronesis-practical-wisdom-20261011.md) |

尚未建立 `insufficient` 卡片；噪声与低质来源已在检索记录的候选边界中登记。

# Branch 询问记录

暂无询问记录。

# Summary 索引

| summary_id | 标题 | status | operation_id | 路径 |
|---|---|---|---|---|
| 20261011-functions-of-knowledge-draft-01 | 知识的功能（draft） | draft / awaiting-confirmation | `op-ai-knowledge-functions-draft-20261011-01` | [`summaries/20261011-functions-of-knowledge-draft-01.md`](summaries/20261011-functions-of-knowledge-draft-01.md) |

draft 由检索 `op-ai-knowledge-functions-search-20261011-01` 派生（父操作），尚未经用户确认，未标记 confirmed。

# 未解决事项

- 各层次概念（信息、知识、理解、能力、判断、智慧）的定义、判据和边界仍未建立；本次只获得方向性候选线索。
- 背景知识促进识别与造成偏见/盲点之间的关系尚无直接证据；本次候选多为“促进理解”，缺少盲点机制来源。
- 所有 8 张证据卡均为摘要级，未经全文核验；方法、样本、效应量与争议未确认。
- 来源噪声明显（词典、商业博客、Wikipedia、推广页、跨领域条目），高质量候选占比有限。
- “知识层级”是否为线性序列存在张力：MDPI 来源标题即为“looking beyond the knowledge hierarchy”，需要在 draft 中保留该不确定性。
- 未找到直接讨论“知识构成可能性边界（可想象/可理解/可验证/可行动）”的候选来源。
- Issue 3–13 不属于本次操作范围，未处理；Issue 1 内容未修改。

# 操作日志

## EVT-20261011-branch-0005：Issue 2 branch 创建

- operation_id: `op-ai-learning-20261011-08`
- event_type: `branch-create`
- occurred_at: `2026-10-11T14:58:35+08:00`
- recorded_at: `2026-10-11T14:58:35+08:00`
- actor: `user + idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-07`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/branch.md`
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/searches/`
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/evidence/`
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/summaries/`
  - `idea-projects/ai-era-human-learning/project.md`
  - `idea-projects/ai-era-human-learning/decisions.md`
  - `idea-projects/ai-era-human-learning/branches/outline.md`
- user_authorization: `授权创建 branch op-ai-learning-20261011-08`
- before: `Issue 2 仅作为 outline 候选存在；目标目录不存在；现有正式 branch_number 最高为 1`
- after: `Issue 2 已创建为 branch_number 2、status=draft、search_status=not-started 的正式 branch；current_branch 保持 why-humans-still-learn`
- not_executed: `未调用 webgo；未创建 evidence 内容；未生成 summary 或 draft；未处理 Issue 3–13；未切换 current_branch`

## EVT-20261011-branch-0006：切换至当前 branch

- operation_id: `op-ai-learning-20261011-09`
- event_type: `branch-switch`
- occurred_at: `2026-10-11T15:06:50+08:00`
- recorded_at: `2026-10-11T15:06:50+08:00`
- actor: `user + idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-08`
- affected_paths:
  - `idea-projects/ai-era-human-learning/project.md`
  - `idea-projects/ai-era-human-learning/decisions.md`
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/branch.md`
- trigger: `branch switch functions-of-knowledge`
- user_authorization: `切换到 branch functions-of-knowledge，并继续生成 webgo 检索计划`
- before: `project.current_branch=why-humans-still-learn；branch status=draft；search_status=not-started`
- after: `project.current_branch=functions-of-knowledge；branch status=draft；search_status=not-started`
- not_executed: `未执行 webgo；未创建检索记录或 evidence；未生成 summary/draft；未处理其他 issue；未改变 branch 状态`

## EVT-20261011-branch-0007：Issue 2 webgo 检索与证据提交

- operation_id: `op-ai-knowledge-functions-search-20261011-01`
- event_type: `search`
- occurred_at: `2026-10-11T15:15:59Z`
- recorded_at: `2026-10-11T15:22:00+08:00`
- actor: `user + idea-navigator + webgo`
- status: `completed`
- parent_operation_id: `op-ai-learning-20261011-09`
- user_authorization: `确认执行检索 op-ai-knowledge-functions-search-20261011-01`
- parameters: `4 queries; itemnums=15 per query; categories=science,general`
- result: `exit_code=0; 4/4 success; returned scales 242,260,226,269; no failed engines reported; noise retained`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/searches/20261011-ai-knowledge-functions-search-01.md`
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/evidence/`
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/branch.md`
- after: `search_status=completed；8 张候选证据卡已落盘；本 branch 检索记录、证据索引与未解决事项已同步`
- evidence_boundary: `全部为搜索摘要级候选证据；未逐篇全文核验；返回数量不计作证据数量`
- not_executed: `未修改 Issue 1；未处理 Issue 3–13；未把 snippet 当作最终事实；未执行全文核验`

## EVT-20261011-branch-0008：Issue 2 draft summary 生成

- operation_id: `op-ai-knowledge-functions-draft-20261011-01`
- event_type: `update`
- occurred_at: `2026-10-11T15:30:00Z`
- recorded_at: `2026-10-11T15:30:00+08:00`
- actor: `idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-knowledge-functions-search-20261011-01`
- trigger: `summary functions-of-knowledge`
- result: `基于 8 张候选证据卡生成探索性 draft，覆盖问题与目标、概念区分、背景知识与认知框架、知识对观察/提问/推理/行动的作用、反方与限制、证据边界和下一步问题`
- summary_status: `draft / awaiting-confirmation`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/summaries/20261011-functions-of-knowledge-draft-01.md`
  - `idea-projects/ai-era-human-learning/branches/2-functions-of-knowledge/branch.md`
- not_executed: `未标记 confirmed；未宣称候选来源已完成全文核验；未修改其他 branch 或 issue`
