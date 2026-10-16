---
project_id: "ai-era-human-learning"
branch_id: "knowledge-transfer-and-application"
branch_number: 8
name: "从理解到能力"
status: draft
question: "知识如何迁移到新问题？"
objective: "研究迁移所需的抽象层次、结构相似性、机制类比与表面类比的区别，以及 AI 如何生成迁移练习并避免虚假类比。"
priority: P1
search_status: completed
evidence_count: 8
summary_count: 1
last_operation_id: "op-ai-transfer-application-draft-20261012-01"
created_at: "2026-10-12T14:41:20+08:00"
updated_at: "2026-10-12T14:41:20+08:00"
operation_id: "op-ai-learning-20261012-21"
parent_operation_id: "op-ai-understanding-validation-draft-20261012-01"
---

# 用户输入

- Issue 8：`knowledge-transfer-and-application`
- 用户原始授权：`授权创建 branch op-ai-learning-20261012-21`
- 用户要求：严格只创建 branch；不执行 webgo、不创建 evidence 内容、不生成 summary/draft、不切换 current_branch、不处理 Issue 9–13。
- 研究问题：知识如何迁移到新问题？
- 目标：研究迁移所需的抽象层次、结构相似性、机制类比与表面类比的区别，以及 AI 如何生成迁移练习并避免虚假类比。

# 已确认内容

- branch_number：8；branch_id：`knowledge-transfer-and-application`；名称：从理解到能力。
- priority：P1；status：`draft`；search_status：`not-started`。
- 本次只创建 branch 容器及同步审计记录。
- `project.current_branch` 保持创建前值 `validating-understanding`。
- searches、evidence、summaries 目录创建为空目录。

# 待确认问题

- “迁移”在本分支中的操作定义：是否包含近迁移、远迁移、跨学科迁移和创造性迁移？
- 抽象层次与结构相似性的判断标准尚未确认。
- AI 生成迁移练习和识别虚假类比的机制、提示策略与人工审核流程尚未确认。
- 与 Issue 5（知识内化）和 Issue 7（理解验证）的边界划分：迁移是否作为内化指标之一，还是独立能力？

# 模型推论

- 当前仅登记研究方向，不将任何迁移学习主张写成已验证事实。
- 表面类比与机制类比的区分可作为后续核心维度；其有效区分方式待后续研究。
- AI 生成迁移练习可能有助于扩展练习空间，但人工判断和领域约束不可或缺。

# 检索记录

- `20261012-transfer-application-search-01`：status=`completed`；operation_id=`op-ai-transfer-application-search-20261012-01`；parent=`op-ai-learning-20261012-22`；四项查询均 `itemnums=15`、`categories=science,general`；返回规模 `200/196/216/157`；检索记录：[`searches/20261012-transfer-application-search-01.md`](searches/20261012-transfer-application-search-01.md)。
- webgo：`exit_code=0`、4/4 success、failed=0、retry=0、elapsed=52.51209016699977 秒；均 `target_reached`、单页；duplicates_removed=`3/1/3/0`；未报告失败引擎；合计候选 769，不等于证据数或研究收敛。

# 证据索引

- `issue8-ev-01-far-transfer-definition-20261012`：近/远迁移定义与边界；supports；[`evidence/01-far-transfer-definition-and-boundary-20261012.md`](evidence/01-far-transfer-definition-and-boundary-20261012.md)。
- `issue8-ev-02-relational-discovery-20261012`：关系发现与远迁移；supports；[`evidence/02-relational-discovery-far-transfer-20261012.md`](evidence/02-relational-discovery-far-transfer-20261012.md)。
- `issue8-ev-03-structural-similarity-analogy-20261012`：结构相似与表面相似；supports；[`evidence/03-structural-similarity-analogy-20261012.md`](evidence/03-structural-similarity-analogy-20261012.md)。
- `issue8-ev-04-analogical-reasoning-structure-mapping-20261012`：类比推理与结构映射；contextual；[`evidence/04-analogical-reasoning-structure-mapping-20261012.md`](evidence/04-analogical-reasoning-structure-mapping-20261012.md)。
- `issue8-ev-05-worked-examples-transfer-20261012`：worked examples 与迁移；supports；[`evidence/05-worked-examples-transfer-20261012.md`](evidence/05-worked-examples-transfer-20261012.md)。
- `issue8-ev-06-variability-practice-transfer-20261012`：变式练习与新题迁移；supports；[`evidence/06-variability-practice-transfer-20261012.md`](evidence/06-variability-practice-transfer-20261012.md)。
- `issue8-ev-07-ai-analogy-false-transfer-20261012`：LLM 虚假类比风险；supports；[`evidence/07-ai-analogy-false-transfer-20261012.md`](evidence/07-ai-analogy-false-transfer-20261012.md)。
- `issue8-ev-08-worked-example-variability-boundaries-20261012`：worked examples/变式的条件边界；contextual；[`evidence/08-worked-example-variability-boundaries-20261012.md`](evidence/08-worked-example-variability-boundaries-20261012.md)。

所有卡均为 webgo 摘要级候选，confidence=`low`；未臆测样本、效应量或因果，保留适用条件、局限和冲突。

# summary 索引

- `20261012-knowledge-transfer-and-application-draft-01`：status=`draft / awaiting-confirmation`；confirmed=`false`；operation_id=`op-ai-transfer-application-draft-20261012-01`；parent=`op-ai-transfer-application-search-20261012-01`；[`summaries/20261012-knowledge-transfer-and-application-draft-01.md`](summaries/20261012-knowledge-transfer-and-application-draft-01.md)。

# 未解决事项

- 8 张候选卡尚未全文获取、逐篇核验、去重和质量评估。
- 近/远迁移的操作化边界及跨研究测量不一致仍未解决。
- 结构相似能否被学习者自发发现、提示对任务性质的影响待核验。
- worked examples、变式水平、先验知识和任务复杂度的条件效应存在待核验冲突。
- AI false analogy 来源的版本、模型、数据集、评价指标和外推范围待核验。
- 与 Issue 5 的内化机制、Issue 7 的理解验证保持边界，不能把本 branch 的迁移判断替代两者。

# 操作日志

## 2026-10-12：Issue 8 webgo—证据—draft

- 检索 operation_id：`op-ai-transfer-application-search-20261012-01`；draft operation_id：`op-ai-transfer-application-draft-20261012-01`。
- 检索 parent：`op-ai-learning-20261012-22`；draft parent：`op-ai-transfer-application-search-20261012-01`。
- 用户授权：`确认执行检索 op-ai-transfer-application-search-20261012-01`。
- webgo 实际状态：`exit_code=0`；4/4 success；候选返回 `200/196/216/157`；failed=0；retry=0；target_reached 四项；去重 `3/1/3/0`；未报告失败引擎。
- 产物提交：检索记录 1、证据卡 8、draft 1，均已写入本 branch；draft 保持 `draft/awaiting-confirmation`、`confirmed=false`。
- not_executed：未执行 Issue 9–13；未修改 Issue 1–7；未创建其他 branch；未切换 current_branch；未全文核验；未把候选结果当最终事实。

## 2026-10-12：Issue 8 branch create

- operation_id：`op-ai-learning-20261012-21`
- event_type：`create`
- occurred_at：`2026-10-12T14:41:20+08:00`
- recorded_at：`2026-10-12T14:41:20+08:00`
- actor：`user + idea-navigator`
- status：`committed`
- parent_operation_id：`op-ai-understanding-validation-draft-20261012-01`
- user_authorization：`授权创建 branch op-ai-learning-20261012-21`
- affected_paths：本 branch 的 branch.md、searches/、evidence/、summaries/，以及项目 project.md、decisions.md、branches/outline.md、MEMORY.md。
- not_executed：`未调用 webgo；未创建 search 记录；未创建 evidence 内容；未生成 summary/draft；未切换 current_branch；未处理 Issue 9–13。`
- validation：`branch_number=8 未占用；目标目录此前不存在；创建后 searches/evidence/summaries 均为空。`

## 2026-10-12：Issue 8 branch switch

- operation_id：`op-ai-learning-20261012-22`
- event_type：`switch`
- occurred_at：`2026-10-12T07:03:57Z`
- recorded_at：`2026-10-12T07:03:57Z`
- actor：`user + idea-navigator`
- status：`committed`
- parent_operation_id：`op-ai-learning-20261012-21`
- user_decision：`切换到 branch knowledge-transfer-and-application，并继续生成 webgo 检索计划`
- before：`project.status=active；current_branch=validating-understanding`
- after：`project.status=active；current_branch=knowledge-transfer-and-application；branch_number=8；status=draft；search_status=not-started`
- affected_paths：`project.md、decisions.md、本 branch.md、MEMORY.md`
- not_executed：`未调用 webgo；未创建检索计划文件、search 记录、evidence 或 summary；未处理 Issue 9–13；未修改 Issue 1–7 研究正文。`
- validation：`Issue 8 branch_number=8、status=draft、search_status=not-started；项目 status=active；current_branch 已切换。`
