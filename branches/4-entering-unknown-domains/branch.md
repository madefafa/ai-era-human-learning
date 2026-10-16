---
project_id: "ai-era-human-learning"
branch_id: "entering-unknown-domains"
branch_number: 4
name: "进入陌生领域"
status: draft
question: "AI 如何帮助人快速进入陌生领域，同时避免产生“已经理解”的错觉？"
objective: "形成术语表、问题树、概念层级、代表性争议和最低背景知识的认知入口模型，重点是地图构建而非资料堆积。"
priority: P1
search_status: completed
evidence_count: 8
summary_count: 1
created_at: "2026-10-12T12:28:58+08:00"
updated_at: "2026-10-12T12:41:30+08:00"
operation_id: "op-ai-learning-20261011-13"
last_operation_id: "op-ai-unknown-domain-draft-20261012-01"
parent_operation_id: "op-ai-unknown-domain-search-20261012-01"
---

# 用户输入

- Issue 4：进入陌生领域。
- 用户授权：`确认执行检索 op-ai-unknown-domain-search-20261012-01`。
- 用户明确边界：严格只处理 Issue 4；不处理 Issue 5–13，不修改 Issue 1–3，不创建其他 branch，不切换 current_branch。

# 已确认内容

- issue_id / branch_id：`entering-unknown-domains`。
- branch_number：`4`。
- 研究问题：AI 如何帮助人快速进入陌生领域，同时避免产生“已经理解”的错觉？
- 目标：形成术语表、问题树、概念层级、代表性争议和最低背景知识的认知入口模型。
- 当前 `project.current_branch` 保持 `entering-unknown-domains`。
- 本次 webgo batch 已完成；候选来源未逐篇全文核验。

# 待确认问题

- “越过入门门槛”“理解”“可迁移掌握”的可观察判据仍需进一步定义。
- 概念地图、术语表、问题树与反例测试的最佳顺序和适用条件尚未证实。
- AI 辅助是否将验证负担系统性转移给陌生领域新手，直接证据不足。
- 不同领域（程序性、身体性、高风险领域）的入口模型是否需要不同版本。

# 模型推论

- 工作模型：陌生领域入口可分为任务边界、术语与最低背景、概念关系、例子/反例、独立验证与迁移五层。
- AI 可作为地图生成、问题生成和反馈工具，但不能替代学习者的独立解释、来源核验和责任判断。
- 以上是基于候选证据的 draft 推论，不构成已核验外部事实。

# 检索记录

| search_id | operation_id | status | queries | itemnums | categories | 返回规模（候选） | 路径 |
|---|---|---|---|---:|---|---|---|
| `20261012-unknown-domain-search-01` | `op-ai-unknown-domain-search-20261012-01` | completed | 4 项 Issue 4 脱敏查询 | 15/项 | science,general | 216 / 142 / 186 / 201 | [`searches/20261012-unknown-domain-search-01.md`](searches/20261012-unknown-domain-search-01.md) |

实际状态：`exit_code=0`，4/4 success，failed_count=0，retry_count=0；均 `target_reached`、`page_count=1`；失败引擎未报告；存在重复合并及词典、博客、推广页、Wikipedia、预印本和未来日期等噪声。返回规模不计作证据数量。

# 证据索引

实际 evidence 文件数：8，与 `evidence_count=8` 一致。

| evidence_id | claim / 主题 | support | confidence | 路径 |
|---|---|---|---|---|
| `pmc-prior-knowledge-concept-maps-20261012` | 先验知识激活与陌生概念连接、概念地图/术语表 | supports | low | [`evidence/pmc-prior-knowledge-concept-maps-20261012.md`](evidence/pmc-prior-knowledge-concept-maps-20261012.md) |
| `ihmc-concept-map-theory-20261012` | 概念及关系外显化；依赖相关先验知识 | contextual | low | [`evidence/ihmc-concept-map-theory-20261012.md`](evidence/ihmc-concept-map-theory-20261012.md) |
| `springer-expertise-reversal-20261012` | 新手脚手架与专业知识逆转 | supports | low | [`evidence/springer-expertise-reversal-20261012.md`](evidence/springer-expertise-reversal-20261012.md) |
| `pmc-illusion-of-knowing-20261012` | 元认知监控与知道/理解错觉 | supports | low | [`evidence/pmc-illusion-of-knowing-20261012.md`](evidence/pmc-illusion-of-knowing-20261012.md) |
| `springer-metacognitive-illusion-20261012` | 元认知错觉与不准确监控 | contextual | low | [`evidence/springer-metacognitive-illusion-20261012.md`](evidence/springer-metacognitive-illusion-20261012.md) |
| `ieee-ai-hallucination-verification-20261012` | AI 流畅生成不等于事实核验 | supports | low | [`evidence/ieee-ai-hallucination-verification-20261012.md`](evidence/ieee-ai-hallucination-verification-20261012.md) |
| `ai-learning-hallucination-review-20261012` | 误导性 AI 输出、额外负荷与过度依赖风险 | contextual | low | [`evidence/ai-learning-hallucination-review-20261012.md`](evidence/ai-learning-hallucination-review-20261012.md) |
| `insufficient-ai-novice-verification-20261012` | AI 陌生领域新手验证问题的直接证据不足 | insufficient | low | [`evidence/insufficient-ai-novice-verification-20261012.md`](evidence/insufficient-ai-novice-verification-20261012.md) |

所有卡片均注明搜索摘要级边界、范围和局限；未将 snippets 当作全文核验事实。

# branch 询问记录

- 当前无独立 ask 操作；本次仅执行用户授权的 webgo—证据—draft 流程。

# summary 索引

| summary_id | operation_id | parent_operation_id | status | 路径 |
|---|---|---|---|---|
| `20261012-entering-unknown-domains-draft-01` | `op-ai-unknown-domain-draft-20261012-01` | `op-ai-unknown-domain-search-20261012-01` | `draft / awaiting-confirmation` | [`summaries/20261012-entering-unknown-domains-draft-01.md`](summaries/20261012-entering-unknown-domains-draft-01.md) |

# 未解决事项

- 8 张证据卡均需逐篇全文核验，尤其是样本、任务、效应、定义、发表状态和限制。
- 需要区分“地图构建工具有效”与“地图等于理解”；概念地图、提取、自我解释、反例测试的相对效果未知。
- AI 辅助陌生领域的直接因果证据不足；验证负担是否转移给新手仍是候选风险而非结论。
- 需要针对不同领域类型和高风险场景确定不同的入口与核验阈值。
- 未经用户确认，summary 不得标记为 `confirmed`；新检索或全文核验需另行授权。

# 操作日志

## EVT-20261012-branch-0014 / branch-create

- operation_id: `op-ai-learning-20261011-13`; status: `committed`；未执行检索、证据或 summary。

## EVT-20261012-branch-0015 / branch-switch

- operation_id: `op-ai-learning-20261011-14`; status: `committed`；current_branch 切换为本 branch；未执行 webgo。

## EVT-20261012-branch-0016 / search-and-evidence

- operation_id: `op-ai-unknown-domain-search-20261012-01`
- event_type: `search + evidence`
- occurred_at / recorded_at: `2026-10-12T12:38:20+08:00`
- actor: `user + idea-navigator + webgo`
- status: `committed`
- parent_operation_id: `op-ai-learning-20261011-14`
- user_authorization: `确认执行检索 op-ai-unknown-domain-search-20261012-01`
- affected_paths: 本 branch 的 search 记录、8 张 evidence cards、branch 索引
- result: `exit_code=0; 4/4 success; returned candidates=216/142/186/201; evidence_count=8`
- not_executed: `未处理 Issue 5–13；未修改 Issue 1–3；未创建其他 branch；未切换 current_branch`

## EVT-20261012-branch-0017 / draft

- operation_id: `op-ai-unknown-domain-draft-20261012-01`
- event_type: `summary-draft`
- occurred_at / recorded_at: `2026-10-12T12:41:30+08:00`
- actor: `idea-navigator`
- status: `committed`
- parent_operation_id: `op-ai-unknown-domain-search-20261012-01`
- affected_paths: 本 branch 的 draft summary、branch 索引
- result: `summary_count=1; status=draft / awaiting-confirmation; confirmed=false`
- not_executed: `未全文核验；未处理 Issue 5–13；未修改 Issue 1–3；未切换 current_branch`
