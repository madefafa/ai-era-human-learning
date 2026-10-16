---
project_id: "ai-era-human-learning"
branch_id: "cross-disciplinary-learning"
branch_number: 11
name: "跨学科学习"
status: draft
question: "AI是连接学科的工具，还是制造表面类比的机器？"
objective: "研究共享概念、映射关系、问题边界、跨域类比有效性与验证，以及工程/科学/社会场景中的跨学科协作案例。"
priority: P2
search_status: completed
evidence_count: 10
summary_count: 1
created_at: "2026-10-12T08:15:34Z"
updated_at: "2026-10-12T08:26:16Z"
last_operation_id: "op-ai-cross-disciplinary-draft-20261012-01"
operation_id: "op-ai-cross-disciplinary-draft-20261012-01"
parent_operation_id: "op-ai-cross-disciplinary-search-20261012-01"
---

# 用户输入

- Issue 11：`cross-disciplinary-learning`
- 用户原始授权（创建）：`授权创建 branch op-ai-learning-20261012-27`
- 用户本轮授权（检索）：`确认执行检索 op-ai-cross-disciplinary-search-20261012-01`
- 用户要求（本轮）：执行已授权的 webgo—证据—draft 流程；严格不得处理 Issue 12–13，不修改 Issue 1–10，不创建其他 branch，不切换 `current_branch`。
- 研究问题：AI 是连接学科的工具，还是制造表面类比的机器？
- 目标：研究共享概念、映射关系、问题边界、跨域类比有效性与验证，以及工程/科学/社会场景中的跨学科协作案例。
- 边界（源自 outline Issue 11）：区分有解释力的类比与仅语言相似的类比；跨域协作的证据边界待研究，不预设 AI 一定能连接学科；**不把跨学科等同知识相加**。

# 已确认内容

- `project_id=ai-era-human-learning`；`branch_id=cross-disciplinary-learning`；`branch_number=11`。
- 名称：跨学科学习；优先级：P2；状态：`draft`。
- 本轮完成一次授权 webgo batch（4 查询）、10 张摘要级候选 evidence cards、1 份 draft；`search_status=completed`、`evidence_count=10`、`summary_count=1`。
- draft 状态 `draft / awaiting-confirmation`，`confirmed=false`。
- `project.current_branch` 保持 `cross-disciplinary-learning`，未切换。
- 研究只登记 Issue 11 的问题、目标和边界；不处理 Issue 12–13。

# 待确认问题

- 跨学科理解需要哪些共享概念、映射关系和问题边界？如何观测与度量？
- 哪些类比具备解释力与可迁移性，哪些只是表面语言相似？“深层结构类比”的判据能否操作化？
- 工程、科学和社会问题中的跨域协作如何验证其有效性？案例入选门槛是什么？
- AI 在跨学科连接中的角色定位：是可靠工具、辅助假设源，还是表面类比生成器？适用与失效条件如何界定？

# 模型推论

- 跨学科理解更像“共享概念 + 结构映射 + 问题边界 + 验证机制”的组合能力，而非知识相加（待验证工作假设）。
- “有解释力的类比”与“仅语言相似的类比”可能通过结构对应、机制一致性、可证伪预测与反例检验来区分；判据与适用范围未确定。
- AI 可充当“跨学科连接候选生成器/假设源”，但连接正确性需外部验证；同一模型自审可能继承自身偏见。
- 上述均为推论；不得写成已验证事实或因果结论。

# 检索记录

## 20261012-cross-disciplinary-search-01

- operation_id：`op-ai-cross-disciplinary-search-20261012-01`；parent_operation_id：`op-ai-learning-20261012-28`；status：`completed`；retrieved_at：`2026-10-12T08:24:30Z`。
- 查询词（4 项，每项 `itemnums=15`、`categories=science,general`）：
  1. `interdisciplinary learning knowledge integration shared concepts boundary mapping`
  2. `analogical reasoning cross domain transfer surface deep structure education`
  3. `interdisciplinary collaboration engineering science social problem solving evidence`
  4. `AI cross disciplinary learning analogy validation hallucination`
- 结果：`exit_code=0`，4/4 success，failed=0，retry=0；返回规模 226/207/200/173（合计 806 候选，非证据数）；均 `target_reached`、1 页；duplicates_removed=1/3/1/0；未报告失败引擎。
- 检索记录路径：[`searches/20261012-cross-disciplinary-search-01.md`](searches/20261012-cross-disciplinary-search-01.md)。

# 证据索引

| # | evidence_id | claim（摘要） | source_title | support | 路径 |
|---:|---|---|---|---|---|
| 01 | 01-conceptual-disambiguation-integration-20261012 | 跨学科整合需概念消歧 | Integrating beyond the surface: conceptual disambiguation and knowledge integration | supports | `evidence/01-conceptual-disambiguation-integration-20261012.md` |
| 02 | 02-boundary-concepts-framework-20261012 | 边界概念/边界对象三阶段框架 | Developing a conceptual framework for interdisciplinary communication... | supports | `evidence/02-boundary-concepts-framework-20261012.md` |
| 03 | 03-boundary-objects-knowledge-integration-review-20261012 | 边界对象与知识整合（依情境） | Boundary objects, knowledge integration, and innovation management: A systematic review | supports | `evidence/03-boundary-objects-knowledge-integration-review-20261012.md` |
| 04 | 04-collaborative-concept-mapping-20261012 | 协作概念图支持跨学科思维 | Supporting interdisciplinary collaborative concept mapping... | contextual | `evidence/04-collaborative-concept-mapping-20261012.md` |
| 05 | 05-deep-structure-vs-surface-features-20261012 | 深层结构 vs 表面特征 | Seeing deep structure from the interactions of surface features | supports | `evidence/05-deep-structure-vs-surface-features-20261012.md` |
| 06 | 06-cross-domain-analogy-structure-creativity-20261012 | 跨域类比=深层结构映射；与创造力相关 | Cross-domain analogical reasoning ability links functional connectome to creativity | supports | `evidence/06-cross-domain-analogy-structure-creativity-20261012.md` |
| 07 | 07-engineering-social-collaboration-framework-20261012 | 工程—社科协作先对齐概念设计 | Framework for interdisciplinary research between engineering and social ... | contextual | `evidence/07-engineering-social-collaboration-framework-20261012.md` |
| 08 | 08-interdisciplinary-team-science-public-20261012 | 跨学科=共同问题+多视角协作 | Interdisciplinary Team Science and the Public | contextual | `evidence/08-interdisciplinary-team-science-public-20261012.md` |
| 09 | 09-ai-analogy-hallucination-risk-20261012 | AI 幻觉=多层技术脆弱性 | New sources of inaccuracy? A conceptual framework for studying AI hallucinations | contextual | `evidence/09-ai-analogy-hallucination-risk-20261012.md` |
| 10 | 10-chain-of-verification-hallucination-20261012 | 验证链降低幻觉（待核验） | Chain-of-Verification Reduces Hallucination in Large Language Models | contextual | `evidence/10-chain-of-verification-hallucination-20261012.md` |

- 汇总：supports=5、contextual=5、insufficient=0；全部为摘要级候选、未全文核验。

# branch 询问记录

- 当前无 branch 询问记录。

# summary 索引

| summary_id | 状态 | confirmed | 路径 |
|---|---|---|---|
| 20261012-cross-disciplinary-learning-draft-01 | draft / awaiting-confirmation | false | `summaries/20261012-cross-disciplinary-learning-draft-01.md` |

- draft operation_id：`op-ai-cross-disciplinary-draft-20261012-01`；parent_operation_id：`op-ai-cross-disciplinary-search-20261012-01`。

# 未解决事项

- 共享概念、映射关系与问题边界的操作化定义与度量尚未确定。
- “深层结构类比”判据（结构对应、机制一致性、可证伪预测、反例检验）尚未操作化与跨领域复核。
- 工程、科学、社会场景中的跨学科协作案例选择标准与候选清单尚未建立。
- AI 角色定位（连接工具 vs 表面类比机器）的直接证据与因果边界待检验；现有材料仅支持“价值与风险并存”的候选陈述。
- 卡 06 存在同题预印本版本，需去重；卡 05 与卡 06 主题重叠需处理。
- 10 张卡均未全文核验；来源层级混杂（预印本、RG、机构页、行业媒体）。
- Issue 11 与 Issue 8（结构映射/类比）存在边界交叉，须保持独立处理；本次不处理 Issue 12–13。

# 操作日志

## 2026-10-12：Issue 11 branch create

- operation_id：`op-ai-learning-20261012-27`；event_type：`create`；status：`committed`；parent_operation_id：`op-ai-machine-knowledge-validation-draft-20261012-01`。
- 创建正式 branch `cross-disciplinary-learning`（branch_number=11，status=draft，search_status=not-started，evidence_count=0，summary_count=0）；未检索、未生成 evidence/summary；current_branch 未切换。

## 2026-10-12：Issue 11 branch switch

- operation_id：`op-ai-learning-20261012-28`；event_type：`switch`；status：`committed`；parent_operation_id：`op-ai-learning-20261012-27`。
- `current_branch`：`validating-machine-generated-knowledge` → `cross-disciplinary-learning`；未检索、未生成 evidence/summary。

## 2026-10-12：Issue 11 webgo—证据—draft

- operation_id（检索）：`op-ai-cross-disciplinary-search-20261012-01`；event_type：`search`；status：`committed`；parent_operation_id：`op-ai-learning-20261012-28`；user_authorization：`确认执行检索 op-ai-cross-disciplinary-search-20261012-01`。
- operation_id（draft）：`op-ai-cross-disciplinary-draft-20261012-01`；event_type：`evidence + summary-draft`；status：`awaiting-confirmation`；parent_operation_id：`op-ai-cross-disciplinary-search-20261012-01`。
- occurred_at：`2026-10-12T08:24:30Z`（检索）/ `2026-10-12T08:26:16Z`（draft）；recorded_at：`2026-10-12T08:26:16Z`；actor：`user + idea-navigator`。
- 执行：一次授权 webgo batch（4 查询×itemnums=15、categories=science,general）；`exit_code=0`、4/4 success、failed=0、retry=0、elapsed≈60.079s；返回 226/207/200/173（806 候选）；均 `target_reached`、1 页；duplicates_removed=1/3/1/0；未报告失败引擎。
- 落盘：search 记录 1 份；候选 evidence cards 10 张（supports=5、contextual=5、insufficient=0）；draft 1 份（`draft / awaiting-confirmation`，confirmed=false）。
- before：`search_status=not-started；evidence_count=0；summary_count=0`；after：`search_status=completed；evidence_count=10；summary_count=1；current_branch 保持 cross-disciplinary-learning`。
- 严格边界：未处理 Issue 12–13；未修改 Issue 1–10 研究正文；未创建其他 branch；未切换 `current_branch`；未执行全文核验或新检索。
- validation：branch_number=11 唯一；searches/evidence/summaries 新增文件数与计数一致；draft confirmed=false；operation_id 唯一且 parent 指向正确。
