---
project_id: "ai-era-human-learning"
branch_id: "knowledge-value-and-selection"
branch_number: 3
name: "高价值知识的识别"
status: draft
question: "什么知识值得投入有限注意力？"
objective: "建立知识价值判断矩阵，区分基础性、解释力、迁移性、可验证性、时效性、实践价值和目标相关性，避免把热度或表达流畅度误认为价值"
priority: "P1"
domain: general
constraints:
  - "区分事实、用户输入、模型推论、待确认问题和未解决事项"
  - "不把热度、表达流畅度或来源权威直接等同于知识价值"
  - "不把模型推论或未来情景写成已确认事实"
  - "不执行外部检索，除非另行展示计划并取得单次明确授权"
assumptions:
  - "有限注意力是知识筛选的核心约束，不同知识在同一目标下的边际价值可能不同"
  - "知识价值可能由多个可区分维度共同决定，而非单一热门程度指标"
  - "基础性、解释力、迁移性、可验证性、时效性、实践价值和目标相关性之间存在需要权衡的张力"
created_at: "2026-10-11T15:29:00+08:00"
updated_at: "2026-10-11T23:41:20+08:00"
initial_operation_id: "op-ai-learning-20261011-10"
parent_operation_id: "op-ai-learning-20261011-09"
search_status: completed
evidence_count: 9
summary_count: 1
last_operation_id: "op-ai-learning-pause-20261011-01"
---

# 用户输入

- 用户明确指定本 branch 对应 Issue 3：`knowledge-value-and-selection`。
- 用户授权原文：`授权创建 branch op-ai-learning-20261011-10`。
- 用户指定名称：`高价值知识的识别`。
- 用户指定问题：`什么知识值得投入有限注意力？`。
- 用户指定目标：`建立知识价值判断矩阵，区分基础性、解释力、迁移性、可验证性、时效性、实践价值和目标相关性，避免把热度或表达流畅度误认为价值。`
- 用户要求只完成 branch 创建，不执行 webgo，不创建 evidence 内容，不生成 summary/draft，不切换 current_branch，不处理 Issue 4–13。
- 用户提供 issue 子问题线索：`基础性、解释力、迁移性、可验证性、时效性、实践价值和目标相关性`；`事实、观点、框架、方法和案例的不同价值`；`如何区分热度、表达流畅度与真实性`。

# 已确认内容

- 本 branch 是项目的第三个正式一级 branch，`branch_number: 3`。
- branch_id 为 `knowledge-value-and-selection`，正式路径为 `branches/3-knowledge-value-and-selection/branch.md`。
- branch 状态为 `draft`，检索状态为 `not-started`，优先级为 `P1`。
- 本次操作仅创建 branch 主文件及空的 `searches/`、`evidence/`、`summaries/` 目录。
- 项目 `current_branch` 创建时为 `functions-of-knowledge`，未自动切换。
- 用户随后明确要求切换：`切换到 branch knowledge-value-and-selection，并继续生成 webgo 检索计划`；已执行 branch switch（`op-ai-learning-20261011-11`），`project.current_branch` 现为 `knowledge-value-and-selection`，项目 status 保持 `active`。
- Issue 4–13 不在本次操作范围，未处理。

# 待确认问题

- 知识价值的候选维度（基础性、解释力、迁移性、可验证性、时效性、实践价值、目标相关性）如何给出可操作的判据与评分方式？
- 各维度之间如何加权与取舍？是否存在“跨场景通用权重”，或权重必须依赖具体目标与时间预算？
- 如何把“事实、观点、框架、方法、案例”映射到价值矩阵的不同维度？
- 如何区分“热度 / 表达流畅度 / 情感煽动”与“真实性 / 可验证性”？
- 可验证性应以什么标准衡量（可复现、可溯源、可反驳、可独立检验）？
- 时效性对“基础性知识”和“前沿事实”是否应有不同的衰减模型？
- 目标相关性如何界定，是否需要一个显式的“目标/问题”输入才能评分？

# 模型推论

以下内容是待论证的工作假设，不是已确认事实：

- 有限注意力意味着知识筛选是一个资源分配问题，价值判断可能更接近多准则权衡而非单指标排序。
- 基础性和解释力倾向于长期稳定，时效性和部分实践价值倾向于随场景与时间衰减，二者可能需要在矩阵中分别处理。
- 热度与传播流畅度是可观测但易被误用的代理指标，可能与被验证的价值弱相关甚至负相关。
- “目标相关性”可能是一个门控维度：脱离目标时，其余维度的绝对评分意义有限。
- 存在高风险情形：高热度 + 高流畅度 + 低可验证性，可能被误判为高价值，需要在矩阵中显式拆分“可信度”与“吸引力”。

# 检索记录

## 检索 20261011-ai-knowledge-value-search-01

- search_id: `20261011-ai-knowledge-value-search-01`
- operation_id: `op-ai-knowledge-value-search-20261011-01`（父操作 `op-ai-learning-20261011-11`）
- 执行时间：`2026-10-11T15:34:49Z`
- 工具：webgo batch（`exit_code=0`）
- 参数：4 项查询，每项 `itemnums=15`、`categories=science,general`
- 查询词：
  1. `knowledge value selection attention explanatory power transfer learning`
  2. `information literacy source credibility relevance evidence evaluation`
  3. `far transfer foundational knowledge learning value`
  4. `curiosity novelty popularity information overload knowledge selection`
- 状态：`completed`（4/4 成功，`failed_count=0`，`retry_count=0`，无失败引擎）
- 返回规模（候选返回条数，非证据数）：`277、211、234、183`；四项均 `stop_reason=target_reached`、`page_count=1`
- 噪声：词典、博客、推广页、电商页、会议论文集，及“迁移学习 vs 学习迁移”语义混淆条目
- 记录路径：`branches/3-knowledge-value-and-selection/searches/20261011-ai-knowledge-value-search-01.md`
- 边界：**evidence cards 未创建、summary 未生成**；未执行全文核验

# 证据索引

本 branch 已执行外部检索 `20261011-ai-knowledge-value-search-01`（completed），并据此建立 **9 张候选证据卡**。全部卡片基于 webgo 返回的标题/摘要（snippet），**未逐篇全文核验**，仅作方向性候选证据；`support`/`contextual` 只表示摘要方向一致，不表示完成质量审查。噪声簇以 `insufficient` 卡片显式登记，未静默删除。

| evidence_id | 主张（简写） | 来源标题 | support | confidence | 路径 |
|---|---|---|---|---|---|
| frontiers-transfer-deep-knowledge-20261011 | 深层基础知识与迁移能力相关 | 深层知识与学习迁移（frontiers 类） | supports | medium | [`evidence/frontiers-transfer-deep-knowledge-20261011.md`](evidence/frontiers-transfer-deep-knowledge-20261011.md) |
| pmc-far-transfer-review-20261011 | 远迁移困难且依赖条件 | 远迁移条件与难度（PMC 类） | contextual | low | [`evidence/pmc-far-transfer-review-20261011.md`](evidence/pmc-far-transfer-review-20261011.md) |
| sciencedirect-proven-source-evaluation-20261011 | 来源可信度评估有结构化模型 | PROVEN / 5Ws&1H 来源评估模型 | supports | medium | [`evidence/sciencedirect-proven-source-evaluation-20261011.md`](evidence/sciencedirect-proven-source-evaluation-20261011.md) |
| acrl-information-literacy-framework-20261011 | 信息素养强调情境化判断权威与价值 | 信息素养框架类来源 | contextual | medium | [`evidence/acrl-information-literacy-framework-20261011.md`](evidence/acrl-information-literacy-framework-20261011.md) |
| pmc-curiosity-information-gain-20261011 | 好奇心与信息增益影响知识获取选择 | 好奇心神经科学与信息增益（PMC 类） | supports | medium | [`evidence/pmc-curiosity-information-gain-20261011.md`](evidence/pmc-curiosity-information-gain-20261011.md) |
| mitpress-novelty-overload-20261011 | 新颖性与信息过载影响选择，吸引注意≠高价值 | 新颖性、信息过载与知识选择（MIT Press 类） | contextual | low | [`evidence/mitpress-novelty-overload-20261011.md`](evidence/mitpress-novelty-overload-20261011.md) |
| semanticscholar-explanatory-power-20261011 | 解释力是可讨论价值属性但判据不清 | 解释力与知识价值/选择（候选） | contextual | low | [`evidence/semanticscholar-explanatory-power-20261011.md`](evidence/semanticscholar-explanatory-power-20261011.md) |
| arxiv-information-selection-attention-20261011 | 有限注意力下选择≈资源分配 | 有限注意力下信息选择（候选） | contextual | low | [`evidence/arxiv-information-selection-attention-20261011.md`](evidence/arxiv-information-selection-attention-20261011.md) |
| noise-cluster-semantic-confusion-20261011 | 本次多数候选为噪声，不能支撑主张 | 检索噪声簇（词典/博客/推广/术语混淆） | insufficient | low | [`evidence/noise-cluster-semantic-confusion-20261011.md`](evidence/noise-cluster-semantic-confusion-20261011.md) |

统计：`support=supports` 3 张、`contextual` 5 张、`insufficient` 1 张；`confidence=medium` 4 张、`low` 5 张。检索返回规模（277/211/234/183）是候选返回条数，**不是**证据数量。

# Branch 询问记录

暂无询问记录。

# Summary 索引

| summary_id | 标题 | status | operation_id | 路径 |
|---|---|---|---|---|
| 20261011-knowledge-value-and-selection-draft-01 | 高价值知识的识别（draft） | draft / awaiting-confirmation | `op-ai-knowledge-value-draft-20261011-01` | [`summaries/20261011-knowledge-value-and-selection-draft-01.md`](summaries/20261011-knowledge-value-and-selection-draft-01.md) |

draft 由检索 `op-ai-knowledge-value-search-20261011-01` 派生（父操作），基于 9 张候选证据卡，尚未经用户确认，未标记 confirmed。

# 未解决事项

- 知识价值矩阵的维度定义、判据、量表（评分区间）和权重规则尚未建立；draft 只提出候选维度与关系，未给出可用量表。
- 各维度之间的冲突与取舍（例如时效性 vs 基础性）尚无处理方案。
- “热度 / 表达流畅度 vs 真实性”区分**缺少直接实证来源**，仅有信息素养框架类候选间接支撑，尚无操作化检测规则。
- 事实、观点、框架、方法、案例的价值差异尚无结构化对照表。
- 本 branch 已完成检索 `20261011-ai-knowledge-value-search-01`（completed），并建立 9 张候选证据卡与 1 份 draft；所有卡片仍为摘要级，**未逐篇全文核验**。
- 迁移性维度证据存在张力：[`frontiers-transfer-deep-knowledge-20261011.md`](evidence/frontiers-transfer-deep-knowledge-20261011.md) 指向深层知识利于迁移，[`pmc-far-transfer-review-20261011.md`](evidence/pmc-far-transfer-review-20261011.md) 提示远迁移困难；二者是否真冲突需全文核验。
- 术语歧义：`transfer learning`（工程）与 `far transfer`（教育心理学）在检索中混淆，导致第 1、3 项查询含较多噪声；需消歧后定向补充检索。
- 覆盖缺口：知识“遮蔽/偏见”面、以及“注意力配置”与“目标相关性门控”缺少直接来源。
- 检索噪声明显（词典/博客/推广页/电商页/语义混淆条目），已以 `insufficient` 卡片登记，未静默删除。
- Issue 4–13 不属于本次操作范围，未处理；Issue 1、Issue 2 内容未修改。

# 操作日志

## EVT-20261011-branch-0009：Issue 3 branch 创建

- operation_id: `op-ai-learning-20261011-10`
- event_type: `branch-create`
- occurred_at: `2026-10-11T15:29:00+08:00`
- recorded_at: `2026-10-11T15:29:00+08:00`
- actor: `user + idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-09`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/branch.md`
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/searches/`
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/evidence/`
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/summaries/`
  - `idea-projects/ai-era-human-learning/project.md`
  - `idea-projects/ai-era-human-learning/decisions.md`
  - `idea-projects/ai-era-human-learning/branches/outline.md`
- user_authorization: `授权创建 branch op-ai-learning-20261011-10`
- before: `Issue 3 仅作为 outline 候选存在；目标目录不存在；现有正式 branch_number 最高为 2`
- after: `Issue 3 已创建为 branch_number 3、status=draft、search_status=not-started 的正式 branch；current_branch 保持 functions-of-knowledge`
- not_executed: `未调用 webgo；未创建 evidence 内容；未生成 summary 或 draft；未处理 Issue 4–13；未切换 current_branch`

## EVT-20261011-branch-0010：切换到本 branch

- operation_id: `op-ai-learning-20261011-11`
- event_type: `switch`
- occurred_at: `2026-10-11T23:31:20+08:00`
- recorded_at: `2026-10-11T23:31:20+08:00`
- actor: `user + idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-10`
- affected_paths:
  - `idea-projects/ai-era-human-learning/project.md`
  - `idea-projects/ai-era-human-learning/decisions.md`
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/branch.md`
- user_decision: `切换到 branch knowledge-value-and-selection，并继续生成 webgo 检索计划`
- before: `project.current_branch=functions-of-knowledge；本 branch status=draft；search_status=not-started`
- after: `project.current_branch=knowledge-value-and-selection；本 branch status=draft；search_status=not-started；project.status=active`
- not_executed: `未调用 webgo；未创建检索记录、evidence 或 summary；未改变本 branch 问题、目标或内容；未切换其他 branch；未处理其他 issue`

## EVT-20261011-branch-0011：Issue 3 检索执行与检索记录落盘（重试）

- operation_id: `op-ai-knowledge-value-search-20261011-01`
- event_type: `search`
- occurred_at: `2026-10-11T15:34:49Z`
- recorded_at: `2026-10-11T23:36:10+08:00`
- actor: `user + idea-navigator + webgo`
- status: `completed`
- parent_operation_id: `op-ai-learning-20261011-11`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/searches/20261011-ai-knowledge-value-search-01.md`
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/branch.md`
- user_authorization: `确认执行检索 op-ai-knowledge-value-search-20261011-01`
- parameters: `4 queries; itemnums=15 per query; categories=science,general`
- result: `exit_code=0; 4/4 successful; returned scales 277,211,234,183; no failed engines; retry_count=0; noise retained`
- before: `search_status=not-started；无检索记录、无证据、无 summary`
- after: `search_status=completed；检索记录已落盘；证据卡与 summary 仍未创建`
- not_executed: `未创建 evidence 卡；未生成 summary/draft；未执行全文核验；未处理 Issue 4–13；未修改 Issue 1/2；未切换 current_branch`

## EVT-20261011-branch-0012：Issue 3 候选证据卡创建

- operation_id: `op-ai-knowledge-value-search-20261011-01`
- event_type: `update`
- occurred_at: `2026-10-11T23:39:00+08:00`
- recorded_at: `2026-10-11T23:39:00+08:00`
- actor: `idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-11`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/evidence/`
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/branch.md`
- result: `创建 9 张候选 evidence 卡；supports 3、contextual 5、insufficient 1；全部为摘要级`
- evidence_boundary: `基于 webgo snippet/标题，未逐篇全文核验；返回规模不是证据数量；噪声以 insufficient 卡显式登记`
- before: `evidence/ 为空；证据索引为“暂无证据卡”`
- after: `evidence/ 含 9 张卡片；证据索引已同步；summary 未生成`
- not_executed: `未调用 webgo；未重新检索；未执行全文核验；未生成 summary/draft；未处理 Issue 4–13；未修改 Issue 1/2；未切换 current_branch`

## EVT-20261011-branch-0013：Issue 3 draft summary 生成

- operation_id: `op-ai-knowledge-value-draft-20261011-01`
- event_type: `update`
- occurred_at: `2026-10-11T23:40:00+08:00`
- recorded_at: `2026-10-11T23:40:00+08:00`
- actor: `idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-knowledge-value-search-20261011-01`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/summaries/20261011-knowledge-value-and-selection-draft-01.md`
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/branch.md`
- result: `生成 draft summary，覆盖价值评价维度、注意力配置、目标依赖、反方与限制、证据边界与候选价值判断矩阵`
- summary_status: `draft / awaiting-confirmation`
- before: `summaries/ 为空；无 summary`
- after: `新增 draft summary；Summary 索引已同步；未标记 confirmed`
- not_executed: `未调用 webgo；未标记 confirmed；未宣称候选来源已完成全文核验；未处理 Issue 4–13；未修改 Issue 1/2；未切换 current_branch`

## EVT-20261011-branch-0014：暂停保存进度的 branch 关联记录

- operation_id: `op-ai-learning-pause-20261011-01`
- event_type: `pause-snapshot`（meta-operation；仅追加本 branch 的暂停关联日志）
- occurred_at: `2026-10-11T23:41:20+08:00`
- recorded_at: `2026-10-11T23:41:20+08:00`
- actor: `user + idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-knowledge-value-draft-20261011-01`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/3-knowledge-value-and-selection/branch.md`
  - `idea-projects/ai-era-human-learning/project.md`
  - `idea-projects/ai-era-human-learning/decisions.md`
  - `idea-projects/ai-era-human-learning/branches/outline.md`
  - `MEMORY.md`
- scope: `本 branch 为暂停时的 current_branch；仅登记暂停关联，不改变本 branch 的任何研究成果`
- before: `本 branch status=draft；search_status=completed；evidence_count=9；summary_count=1；current_branch=knowledge-value-and-selection`
- after: `本 branch status=draft（未改动）；search_status=completed（未改动）；evidence_count=9（未改动）；summary_count=1（未改动）；current_branch=knowledge-value-and-selection（未改动）`
- not_executed: `未调用 webgo；未创建 evidence 或 summary；未重新检索；未执行全文核验；未处理 Issue 4–13；未切换 current_branch；未改写既有 EVT-0009～0013 历史记录`
- resume_note: `恢复后本 branch 的 draft summaries/20261011-knowledge-value-and-selection-draft-01.md 待用户确认或修订；全文核验与消歧检索须另行授权`
