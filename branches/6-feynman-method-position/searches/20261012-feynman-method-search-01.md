---
search_id: "20261012-feynman-method-search-01"
project_id: "ai-era-human-learning"
branch_id: "feynman-method-position"
branch_number: 6
operation_id: "op-ai-feynman-method-search-20261012-01"
parent_operation_id: "op-ai-learning-20261012-18"
status: completed
actor: "user + idea-navigator + webgo"
trigger: "执行 Issue 6 完整 webgo—证据—draft 流程"
retrieved_at: "2026-10-12T05:41:30Z"
exit_code: 0
requested_count: 4
completed_count: 4
failed_count: 0
retry_count: 0
elapsed_seconds: 60.104525042000205
categories: "science,general"
itemnums_per_query: 15
candidate_count_total: 785
returned_itemnums: [206, 202, 202, 175]
---

# 检索计划与授权

- 当前 branch：`feynman-method-position`；研究问题：费曼解释法是工具、指标，还是学习理论？
- 用户授权原文：`确认执行检索 op-ai-feynman-method-search-20261012-01`
- 父操作：`op-ai-learning-20261012-18`
- 每项 `itemnums=15`、`categories=science,general`。
- 检索仅针对 Issue 6；不处理 Issue 7–13、不修改 Issue 1–5、不创建 branch、不切换 current_branch。

# Webgo batch 执行结果

顶层结果：`exit_code=0`，requested/completed/failed=`4/4/0`，retry_count=`0`，elapsed_seconds=`60.104525042000205`，success_rate=`1.0`、failure_rate=`0.0`。

| # | Query | 状态 | 返回规模 | Diagnostics | 失败引擎 |
|---|---|---|---:|---|---|
| 1 | `self explanation learning outcomes meta analysis explaining to learn` | success | 206 candidates/items | stop_reason=`target_reached`; page_count=1; duplicates_removed=3 | 未报告 |
| 2 | `Feynman technique evidence learning science self explanation limitations` | success | 202 candidates/items | stop_reason=`target_reached`; page_count=1; duplicates_removed=1 | 未报告 |
| 3 | `self explanation practice performance transfer expertise learning` | success | 202 candidates/items | stop_reason=`target_reached`; page_count=1; duplicates_removed=1 | 未报告 |
| 4 | `retrieval practice feedback worked examples learning strategy comparison` | success | 175 candidates/items | stop_reason=`target_reached`; page_count=1; duplicates_removed=2 | 未报告 |

合计候选返回规模 785。`returned_itemnums`/`item_count` 表示检索响应候选规模，绝不等同于已核验来源数或证据卡数量；batch `itemnums=15` 也不应据此误读候选计数。失败引擎字段未在响应中提供，按“未报告”记录，不推断无引擎问题。

# 候选发现与证据边界

- 自我解释元分析的摘要/二手报道提到涵盖 64 项研究、约 6000 名参与者，平均效应量约 Hedges' g=0.55；仍需核对原始论文、异质性、任务及发表偏倚，现阶段只能作待核候选。
- 检索到 Springer 的 `Inducing self-explanation: A meta-analysis`（https://link.springer.com/article/10.1007/s10648-018-9434-x），以及数学自我解释元分析和数字学习环境三层元分析候选；摘要不足以支持跨领域的普遍因果断言。
- 没有发现可据此确认“费曼技巧”作为完整命名流程拥有直接、独立的实验验证。搜索结果里相关指南/博客多为实践性介绍；这不等价于该整体方法无效，也不构成验证。
- Frontiers 2018 的自我解释与批判性思维学习/迁移文章摘要报告部分练习任务后测出现负效应，另有任务未见效；它提示结果依任务而异，需读全文确认设计和效应。
- 检索到自我解释与直接教学/迁移研究候选，以及检索练习与 worked examples（解题示例）的目标依赖比较。结果支持把策略选择、先备知识、任务目标、练习和反馈作为边界条件，而不是把单一策略宣称为唯一/充分方法。
- 结果噪声包括学习技巧博客/商业页面、论坛问答、词典、百科条目、无关网页、预印本，以及日期/质量需核验的条目；检索摘要可能不完整或失真。

# 候选证据卡和 draft 状态

- evidence 状态：待从候选中筛选并创建 6–10 张卡。仅搜索摘要支撑的内容降低置信度；不把二手报道或方法指南升级为原始研究结论。
- draft 状态：待创建 `summaries/20261012-feynman-method-position-draft-01.md`，目标状态 `draft/awaiting-confirmation`，不得标为 confirmed。

# 用户汇报摘要

实际 webgo batch 全部成功（`exit_code=0`，4/4 success，0 failed，0 retry）；四项候选规模依次为 206、202、202、175，共 785 条候选响应记录，不是 785 项证据。各项均单页、达到工具 stop target，去重数依次为 3、1、1、2；响应未报告失败引擎。候选线索涉及自我解释元分析、迁移与练习任务表现、检索练习/反馈和示例学习对照；费曼技巧整体缺少由本次结果直接核实的独立研究证据。噪声含商业/博客指南、论坛、词典/百科、无关条目和待核日期/质量的资料。下一步建立 8 张候选证据卡，摘要证据保守降级并标出全文核验需求；再生成未确认 draft。检索记录已持久化；此记录写入时 evidence 与 draft 仍为 pending，后续状态将由同一操作同步更新。

# 操作日志

- operation_id：`op-ai-feynman-method-search-20261012-01`
- parent_operation_id：`op-ai-learning-20261012-18`
- authorization：`确认执行检索 op-ai-feynman-method-search-20261012-01`
- status：webgo 执行成功；证据卡和 draft 创建阶段尚待完成。
