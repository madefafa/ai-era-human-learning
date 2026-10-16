---
project_id: "ai-era-human-learning"
branch_id: "human-ai-learning-collaboration"
branch_number: 9
name: "人与AI的分工"
status: draft
question: "在人机协同学习中，哪些环节适合交给AI，哪些环节必须由人保留？"
objective: "形成学习过程中的人机职责分配表或协同流程，区分检索、压缩、比较、模拟、提问、反例生成与目标、价值、边界、证据要求、最终判断和责任。"
priority: P1
search_status: completed
evidence_count: 8
summary_count: 1
last_operation_id: "op-ai-human-ai-collab-draft-20261012-01"
created_at: "2026-10-12T07:18:45Z"
updated_at: "2026-10-12T07:40:56Z"
operation_id: "op-ai-learning-20261012-23"
parent_operation_id: "op-ai-learning-20261012-22"
---

# 用户输入

- Issue 9：`human-ai-learning-collaboration`
- 用户原始授权：`授权创建 branch op-ai-learning-20261012-23`
- 用户要求：严格只创建 branch；不执行 webgo、不创建 evidence 内容、不生成 summary/draft、不切换 current_branch、不处理 Issue 10–13。
- 研究问题：在人机协同学习中，哪些环节适合交给 AI，哪些环节必须由人保留？
- 目标：形成学习过程中的人机职责分配表或协同流程，区分检索、压缩、比较、模拟、提问、反例生成与目标、价值、边界、证据要求、最终判断和责任。

# 已确认内容

- branch_number：9；branch_id：`human-ai-learning-collaboration`；名称：人与AI的分工。
- priority：P1；status：`draft`；search_status：`not-started`。
- 本次只创建 branch 容器及同步审计记录。
- `project.current_branch` 保持创建前值 `knowledge-transfer-and-application`。
- `searches/`、`evidence/`、`summaries/` 创建为空目录，暂不写入任何研究产物。
- 研究范围聚焦学习过程中的人机职责边界，不扩展处理 Issue 10–13。

# 待确认问题

- “适合交给 AI”的判断标准：效率、可验证性、可逆性、错误代价和学习收益如何排序？
- 检索、压缩、比较、模拟、提问、反例生成等环节的人工复核点和证据要求尚未确认。
- 目标设定、价值排序、边界定义、证据标准、最终判断与责任承担的操作化方式尚未确认。
- 如何识别“辅助思考”与“把思考外包给 AI”的分界，以及如何保留学习者的独立重建与判断？

# 模型推论

- 当前仅登记研究方向，不将任何关于人或 AI 能力边界的主张写成已验证事实。
- 后续可将学习流程拆分为任务委托、人工设定约束、AI 生成候选、人工核验与最终负责等阶段；该流程只是待验证的工作假设。
- AI 与人的分工可能随任务风险、可验证性、领域知识和学习目标变化，不能预设一套跨场景固定分工。

# 检索记录

- 当前无检索记录。
- `search_status=not-started`；本次未生成检索计划，未调用 webgo。

# 证据索引

- 本次新增 8 张摘要级候选 evidence cards；均未全文核验。
- [01-cognitive-offloading-student-ai-20261012](evidence/01-cognitive-offloading-student-ai-20261012.md)：认知外包与学生—AI 协同，supports，confidence=medium。
- [02-cognitive-offloading-boundary-20261012](evidence/02-cognitive-offloading-boundary-20261012.md)：认知外包的增强/侵蚀边界，contextual，confidence=medium。
- [03-metacognition-agency-judgment-20261012](evidence/03-metacognition-agency-judgment-20261012.md)：agency、透明度、元认知与学习者选择，contextual，confidence=low。
- [04-judgment-of-learning-human-ability-20261012](evidence/04-judgment-of-learning-human-ability-20261012.md)：学习判断与人类监督候选，contextual，confidence=low。
- [05-delegation-verification-critical-thinking-20261012](evidence/05-delegation-verification-critical-thinking-20261012.md)：分析过程委托与 verification，supports，confidence=medium。
- [06-critical-thinking-ai-use-scale-20261012](evidence/06-critical-thinking-ai-use-scale-20261012.md)：AI 使用中的 verification/反思判断，supports，confidence=medium。
- [07-human-ai-task-allocation-20261012](evidence/07-human-ai-task-allocation-20261012.md)：automation/augmentation 与任务分配，supports，confidence=medium。
- [08-complementary-policies-human-ai-teams-20261012](evidence/08-complementary-policies-human-ai-teams-20261012.md)：互补策略与战略分工，contextual，confidence=low。

# branch 询问记录

- 当前无 branch 询问记录。

# summary 索引

- [20261012-human-ai-learning-collaboration-draft-01](summaries/20261012-human-ai-learning-collaboration-draft-01.md)：Issue 9 协同职责、外包边界与监督流程 draft；状态 `awaiting-confirmation`，confirmed=false；operation_id=`op-ai-human-ai-collab-draft-20261012-01`。

# 未解决事项

- 8 张摘要级候选卡需全文核验研究设计、样本/任务、测量、结果与适用边界；不能将摘要升级为事实或因果证据。
- 需处理跨查询重复与潜在冲突，尤其是认知外包的增强/侵蚀、delegation 后 verification 的实际学习效果。
- 不同学习者（先验知识、年龄、学科、AI 素养、动机）对职责分配和监督质量的影响尚未知。
- 监督质量需操作化：来源核验、推理核验、独立重建、反例压力测试和最终判断不能混为一项。
- 直接教育实证不足；部分候选来自一般决策/工作、预印本、ResearchGate 或媒体/博客层级。
- Issue 9 与 Issue 10（机器生成知识可信度）、Issue 12（主体性与责任）的边界留待后续独立处理；本次不处理 Issue 10–13。

# 操作日志

## 2026-10-12：Issue 9 branch create

- operation_id：`op-ai-learning-20261012-23`
- event_type：`create`
- occurred_at：`2026-10-12T07:18:45Z`
- recorded_at：`2026-10-12T07:18:45Z`
- actor：`user + idea-navigator`
- status：`committed`
- parent_operation_id：`op-ai-learning-20261012-22`
- user_authorization：`授权创建 branch op-ai-learning-20261012-23`
- affected_paths：本 branch 的 `branch.md`、`searches/`、`evidence/`、`summaries/`，以及项目 `project.md`、`decisions.md`、`branches/outline.md`、`MEMORY.md`。
- not_executed：`未调用 webgo；未创建 search 记录；未创建 evidence 内容；未生成 summary/draft；未切换 current_branch；未处理 Issue 10–13。`
- validation：`branch_number=9 未占用；目标目录此前不存在；创建后 searches/evidence/summaries 均为空；current_branch 保持 knowledge-transfer-and-application。`

## 2026-10-12：Issue 9 branch switch

- operation_id：`op-ai-learning-20261012-24`
- event_type：`switch`
- occurred_at：`2026-10-12T07:23:17Z`
- recorded_at：`2026-10-12T07:23:17Z`
- actor：`user + idea-navigator`
- status：`committed`
- parent_operation_id：`op-ai-learning-20261012-23`
- user_input：`切换到 branch human-ai-learning-collaboration，并继续生成 webgo 检索计划`
- before：`project.status=active；current_branch=knowledge-transfer-and-application`
- after：`project.status=active；current_branch=human-ai-learning-collaboration；branch_number=9；status=draft；search_status=not-started`
- not_executed：`未调用 webgo；未创建检索计划文件、search 记录、evidence 或 summary；未处理 Issue 10–13；未修改 Issue 1–8 研究正文`
- validation：`Issue 9 三类产物目录无新增文件；研究正文未修改`

## 2026-10-12：Issue 9 webgo—证据—draft

- 检索 operation_id：`op-ai-human-ai-collab-search-20261012-01`；parent=`op-ai-learning-20261012-24`；用户授权：`确认执行检索 op-ai-human-ai-collab-search-20261012-01`。
- webgo：`exit_code=0`，4/4 success，failed=0，retry=0；返回规模 `166/149/179/193`，合计 687；均 `target_reached`、1 页；duplicates_removed=`4/0/0/4`；失败引擎未报告。
- 检索记录：`searches/20261012-human-ai-collab-search-01.md`；证据卡 8 张；draft `summaries/20261012-human-ai-learning-collaboration-draft-01.md`。
- draft operation_id=`op-ai-human-ai-collab-draft-20261012-01`；parent=`op-ai-human-ai-collab-search-20261012-01`；状态=`awaiting-confirmation`、confirmed=false。
- 严格边界：未处理 Issue 10–13；未修改 Issue 1–8；未创建其他 branch；未切换 current_branch；未全文核验。


## 2026-10-12：Issue 9 webgo—证据—draft

- 检索 operation_id：`op-ai-human-ai-collab-search-20261012-01`；parent=`op-ai-learning-20261012-24`；用户授权：`确认执行检索 op-ai-human-ai-collab-search-20261012-01`。
- webgo：`exit_code=0`，4/4 success，failed=0，retry=0；返回规模 `166/149/179/193`，合计 687；均 `target_reached`、1 页；duplicates_removed=`4/0/0/4`；失败引擎未报告。
- 检索记录：`searches/20261012-human-ai-collab-search-01.md`。
- 候选证据卡：8 张，摘要级；supports=4、contextual=4、insufficient=0；覆盖认知外包、元认知/agency/判断、delegation/verification、互补性/任务分配。
- draft：`summaries/20261012-human-ai-learning-collaboration-draft-01.md`；operation_id=`op-ai-human-ai-learning-collab-draft-20261012-01`；parent=`op-ai-human-ai-learning-collab-search-20261012-01`；状态=`awaiting-confirmation`、confirmed=false。
- 严格边界：未处理 Issue 10–13；未修改 Issue 1–8；未创建其他 branch；未切换 current_branch；未全文核验。
- 未解决：8 张卡全文核验、研究设计/样本/效应量核对、跨查询去重与冲突、学习者差异、监督质量操作化、教育场景直接证据不足。
