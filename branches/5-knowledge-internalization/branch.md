---
project_id: "ai-era-human-learning"
branch_id: "knowledge-internalization"
branch_number: 5
name: "知识内化的机制"
status: draft
question: "外部内容如何变成自己的理解？"
objective: "建立知识内化的可观察指标体系，覆盖概念结构、因果解释、独立复述、反例辨析、迁移应用和错误修正。"
priority: P0
search_status: completed
constraints:
  - "本次仅处理 Issue 5。"
  - "不处理 Issue 6–13。"
  - "不修改 Issue 1–4。"
  - "不创建其他 branch，不切换 current_branch。"
assumptions: []
evidence_count: 9
summary_count: 1
created_at: "2026-10-12T04:50:00Z"
updated_at: "2026-10-12T05:21:45Z"
operation_id: "op-ai-learning-20261012-15"
last_operation_id: "op-ai-internalization-draft-20261012-01"
---

# 用户输入

- Issue 5：`knowledge-internalization`
- branch_number：5
- branch_id：`knowledge-internalization`
- name：知识内化的机制
- question：外部内容如何变成自己的理解？
- objective：建立知识内化的可观察指标体系，覆盖概念结构、因果解释、独立复述、反例辨析、迁移应用和错误修正。
- priority：P0
- 用户授权：`授权创建 branch op-ai-learning-20261012-15`

# 已确认内容

- 已确认创建项目 `ai-era-human-learning` 的 Issue 5 正式 branch。
- 已确认 branch_number=5、branch_id=`knowledge-internalization`、status=`draft`。
- 已确认 `search_status=completed`；检索、证据卡和 draft 均仅作用于 Issue 5。
- 已确认本次检索 operation_id 为 `op-ai-internalization-search-20261012-01`，draft operation_id 为 `op-ai-internalization-draft-20261012-01`。
- 已确认保留项目 `current_branch=knowledge-internalization`，本次不执行 branch switch。

# 待确认问题

- 暂无。本区块仅记录 branch 创建阶段尚未确认的事项；后续研究范围、证据标准和指标操作化细节需另行确认。

# 模型推论

- 本 branch 的后续研究可围绕六类可观察表现组织：概念结构、因果解释、独立复述、反例辨析、迁移应用和错误修正。
- 上述内容是基于用户目标的结构化推论，不是外部证据或已验证结论。

# 检索记录

- `20261012-knowledge-internalization-search-01`：status=`completed`；operation_id=`op-ai-internalization-search-20261012-01`；parent=`op-ai-learning-20261012-16`；4/4 success；`exit_code=0`；returned candidates=`181/184/169/212`，合计 746，不等于证据数量；每项 `target_reached`、1 页；duplicates_removed=`1/0/5/0`；未报告失败引擎。
- 查询参数均为 `itemnums=15`、`categories=science,general`；主要方向为概念理解/因果解释、自我解释/主动提取/概念改变、元认知监控/流畅性错觉、迁移/反馈/错误修正。
- 噪声包括博客、商业页、Wikipedia、ResearchGate、预印本、多语言和明显无关条目；未执行全文核验、效应量提取或系统筛选。
- 检索记录：[`searches/20261012-knowledge-internalization-search-01.md`](searches/20261012-knowledge-internalization-search-01.md)

# 证据索引

| evidence_id | claim focus | support | confidence | path |
|---|---|---|---|---|
| `narst-conceptual-understanding-transfer-20261012` | 概念结构与迁移 | supports | low | [`evidence/narst-conceptual-understanding-transfer-20261012.md`](evidence/narst-conceptual-understanding-transfer-20261012.md) |
| `frontiers-causal-explanation-internalization-20261012` | 互动解释与因果逻辑 | contextual | low | [`evidence/frontiers-causal-explanation-internalization-20261012.md`](evidence/frontiers-causal-explanation-internalization-20261012.md) |
| `mit-retrieval-explanation-integration-20261012` | 主动提取与自我解释 | supports | low | [`evidence/mit-retrieval-explanation-integration-20261012.md`](evidence/mit-retrieval-explanation-integration-20261012.md) |
| `apa-misconceptions-conceptual-change-20261012` | 错误概念与概念改变 | contextual | low | [`evidence/apa-misconceptions-conceptual-change-20261012.md`](evidence/apa-misconceptions-conceptual-change-20261012.md) |
| `pmc-metacognitive-monitoring-fluency-20261012` | 元认知监控与熟悉感错觉 | contextual | low | [`evidence/pmc-metacognitive-monitoring-fluency-20261012.md`](evidence/pmc-metacognitive-monitoring-fluency-20261012.md) |
| `pmc-deliberate-erring-far-transfer-20261012` | 主动错误、修正与远迁移 | supports | low | [`evidence/pmc-deliberate-erring-far-transfer-20261012.md`](evidence/pmc-deliberate-erring-far-transfer-20261012.md) |
| `butler-explanation-feedback-transfer-20261012` | 解释性反馈与迁移 | supports | low | [`evidence/butler-explanation-feedback-transfer-20261012.md`](evidence/butler-explanation-feedback-transfer-20261012.md) |
| `springer-deliberate-erring-transfer-20261012` | 迁移边界与重复来源 | contextual | low | [`evidence/springer-deliberate-erring-transfer-20261012.md`](evidence/springer-deliberate-erring-transfer-20261012.md) |
| `noisy-search-result-internalization-20261012` | 检索噪声审计 | insufficient | high | [`evidence/noisy-search-result-internalization-20261012.md`](evidence/noisy-search-result-internalization-20261012.md) |

# branch 询问记录

- 暂无 branch 询问记录。

# summary 索引

- `20261012-knowledge-internalization-draft-01`：status=`draft`、review_status=`awaiting-confirmation`、confirmed=`false`；operation_id=`op-ai-internalization-draft-20261012-01`；parent=`op-ai-internalization-search-20261012-01`；路径：[`summaries/20261012-knowledge-internalization-draft-01.md`](summaries/20261012-knowledge-internalization-draft-01.md)

# 未解决事项

- 9 张卡均为搜索摘要级候选材料，需逐篇全文核验，不能将候选摘要写成已确认事实。
- 需要去重并确认 PMC/Springer 相关结果是否为同一研究，补充原始研究、综述、样本、效应量和边界条件。
- 六类指标的定义、评分方式、最小任务和跨领域适用边界尚未验证。
- 需要测试 AI 流畅输出、主动提取、解释反馈与独立迁移之间的差异，避免把 AI 辅助等同于学习者内化。
- draft 尚未用户确认，不得标记为 `confirmed`。

# 操作日志

## 2026-10-12T04:50:00Z — branch-create

- operation_id: `op-ai-learning-20261012-15`
- actor: `user`
- status: `committed`
- event_type: `branch-create`
- authorization: `授权创建 branch op-ai-learning-20261012-15`
- affected_paths:
  - `idea-projects/ai-era-human-learning/branches/5-knowledge-internalization/branch.md`
  - `idea-projects/ai-era-human-learning/branches/5-knowledge-internalization/searches/`
  - `idea-projects/ai-era-human-learning/branches/5-knowledge-internalization/evidence/`
  - `idea-projects/ai-era-human-learning/branches/5-knowledge-internalization/summaries/`
- parent_operation_id: `op-ai-unknown-domain-draft-20261012-01`
- executed:
  - "创建 branch.md。"
  - "创建空的 searches/、evidence/、summaries/ 目录。"
- not_executed:
  - "未执行 webgo。"
  - "未创建 evidence 内容。"
  - "未生成 summary/draft。"
  - "未切换 current_branch。"
  - "未处理 Issue 6–13。"
- validation:
  - "目标路径创建前不存在。"
  - "branch_number=5 未被既有 branch 占用。"

## 2026-10-12T04:55:41Z — branch-switch

- operation_id: `op-ai-learning-20261012-16`
- actor: `user + idea-navigator`
- status: `committed`
- event_type: `branch-switch`
- authorization: `切换到 branch knowledge-internalization，并继续生成 webgo 检索计划；本次仅执行 branch switch`
- affected_paths:
 - `idea-projects/ai-era-human-learning/project.md`
 - `idea-projects/ai-era-human-learning/decisions.md`
 - `idea-projects/ai-era-human-learning/branches/5-knowledge-internalization/branch.md`
 - `MEMORY.md`
- parent_operation_id: `op-ai-learning-20261012-15`
- before: `project.status=active；current_branch=entering-unknown-domains`
- after: `project.status=active；current_branch=knowledge-internalization；branch_number=5；status=draft；search_status=not-started`
- executed:
 - "仅切换项目 current_branch。"
- not_executed:
 - "未调用 webgo。"
 - "未生成 webgo 检索计划文件。"
 - "未创建 search 记录、evidence 内容或 summary/draft。"
 - "未修改 Issue 5 研究内容。"
 - "未处理 Issue 6–13 或其他 issue。"
- validation:
  - "searches/、evidence/、summaries/ 目录保持为空。"

## 2026-10-12T05:18:31Z — webgo—evidence—draft

- operation_id: `op-ai-internalization-draft-20261012-01`
- parent_operation_id: `op-ai-internalization-search-20261012-01`
- actor: `user + idea-navigator + webgo`
- status: `committed`
- event_type: `search + evidence + summary-draft`
- authorization: `确认执行检索 op-ai-internalization-search-20261012-01`
- affected_paths:
  - `searches/20261012-knowledge-internalization-search-01.md`
  - `evidence/`（9 张候选卡）
  - `summaries/20261012-knowledge-internalization-draft-01.md`
  - `branch.md`
  - `project.md`
  - `decisions.md`
  - `MEMORY.md`
- webgo_result: `exit_code=0; 4/4 success; failed_count=0; retry_count=0; returned=181/184/169/212; total=746; diagnostics=target_reached, page_count=1, duplicates_removed=1/0/5/0; failed_engines=none reported`
- evidence_result: `9 cards; supports=4; contextual=4; insufficient=1; search-summary level; confidence mostly low`
- draft_result: `status=draft; review_status=awaiting-confirmation; confirmed=false; summary_count=1`
- not_executed:
  - "Issue 6–13。"
  - "Issue 1–4 内容修改。"
  - "创建其他 branch 或切换 current_branch。"
  - "全文核验、系统筛选和新检索。"
- validation:
  - "project.current_branch 保持 knowledge-internalization。"
  - "branch_number=5；evidence_count=9；summary_count=1。"
