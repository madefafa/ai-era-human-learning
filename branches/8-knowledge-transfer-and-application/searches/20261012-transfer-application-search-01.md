---
search_id: "20261012-transfer-application-search-01"
branch_id: "knowledge-transfer-and-application"
branch_number: 8
status: completed
operation_id: "op-ai-transfer-application-search-20261012-01"
parent_operation_id: "op-ai-learning-20261012-22"
authorization: "确认执行检索 op-ai-transfer-application-search-20261012-01"
retrieved_at: "2026-10-12T07:09:57Z"
itemnums: 15
categories: "science,general"
---

# 检索目的

围绕“知识如何迁移到新问题”，收集近/远迁移、抽象与结构相似、类比推理、worked examples 与变式练习，以及 AI 生成迁移任务和虚假类比的候选来源。检索结果仅作为候选来源索引，不等同于已核验的证据或研究收敛。

# 授权与参数

- 用户授权：`确认执行检索 op-ai-transfer-application-search-20261012-01`
- 检索 operation_id：`op-ai-transfer-application-search-20261012-01`
- 父操作：`op-ai-learning-20261012-22`
- 四项查询均使用 `itemnums=15`、`categories=science,general`。
- webgo 返回每项 `target_reached`，但实际返回规模高于请求的 itemnums；返回规模是候选结果规模，不是证据数量。

# Webgo 实际状态

- 总体 `exit_code=0`；`requested_count=4`、`completed_count=4`、`failed_count=0`；success_rate=1.0、failure_rate=0.0、retry_count=0；elapsed_seconds=52.51209016699977。
- 失败引擎：未报告失败引擎。

| # | query | status | returned_itemnums / item_count | stop_reason | page_count | duplicates_removed |
|---:|---|---|---:|---|---:|---:|
| 1 | near far transfer learning mechanism abstraction structural similarity education | success | 200 / 200 | target_reached | 1 | 3 |
| 2 | analogical reasoning surface deep structure transfer problem solving | success | 196 / 196 | target_reached | 1 | 1 |
| 3 | worked examples transfer practice variation learning | success | 216 / 216 | target_reached | 1 | 3 |
| 4 | AI generated transfer tasks analogical reasoning false analogy learning | success | 157 / 157 | target_reached | 1 | 0 |

合计候选返回规模：769；此数不是证据卡数量，也不表示研究已收敛。

# 候选来源索引与初步判断

1. **近/远迁移与结构相似**：Taylor & Francis 的 far transfer 定义文章；PMC 的 retrieval-practice far transfer 研究；ERIC 的 transfer theories/practices 综述 PDF；Frontiers 的 relational discovery/far transfer 研究；Cognitive Science/教育来源若干。
2. **类比推理与结构映射**：Stanford Encyclopedia of Philosophy 的 analogy 条目；Gentner/Smith 的 analogical reasoning PDF；Surface and structural similarity in analogical transfer；Knowledge Representations/novel problem solving 研究；Gick/Holyoak 相关书目线索。
3. **worked examples 与变式练习**：worked examples 与 retention/transfer 研究；Springer/NSF 的 variability、retrieval practice 和 worked examples 线索；test item variation 与 transfer 研究；几何问题 worked examples variability 线索。
4. **AI 生成迁移任务与虚假类比**：arXiv “Can LLMs Help Improve Analogical Reasoning for Strategic Decisions?”；INFORMS 版本线索；Cambridge 的 LLM analogical reasoning benchmark；MDPI transfer learning/analogical inference 综述；IBM 解释性条目仅作背景。

# 无关、重复与语义混淆登记

- 无关结果：房地产/政府 transfer、英文词典、英语词频、疫情页面、AI 艺术页面、招生 transfer essay、泛 AI 产品营销、CSDN/Medium/商业博客等。
- 重复/交叉：多个查询重复出现 Encyclopedia of Cognitive Sciences、Transfer of Learning Examples、Stanford analogy 条目以及相同书目/聚合页；重复由 webgo 部分去除，但跨查询重复仍需人工处理。
- 语义混淆：`transfer` 被解释为政府转移支付、房产转让、大学转学或一般技术 transfer；`AI-generated` 被扩展为 AI 艺术、AI 产品推荐；部分结果是算法迁移学习而非人类学习迁移。
- 质量风险：部分结果来自 ResearchGate、聚合/跳转 URL、博客、预印本或仅有摘要；日期与全文状态需核验。

# 用户汇报摘要

webgo batch 实际成功 4/4，exit_code=0，无失败项、无报告失败引擎，四项候选规模为 200、196、216、157，合计 769；均单页 target_reached，去重数为 3、1、3、0。候选初步覆盖迁移定义、结构映射、worked examples/变式练习和 AI 类比推理，但包含大量词典、商业、技术 transfer、无关 transfer 及聚合结果。当前仅据搜索摘要建立候选 evidence cards；不把返回数量、target_reached 或 snippet 视为证据数量、研究收敛、全文事实、样本、效应量或因果结论。

# 落盘状态

- 本检索记录：已落盘。
- 候选证据卡：随后在同一 branch 的 `evidence/` 创建，目标 8 张；均标注摘要级边界。
- draft：随后创建，状态 `draft / awaiting-confirmation`，`confirmed=false`。
- branch/project/decisions/MEMORY：随后同步；若同步失败，应保留已写文件并标记 partial，不得假称 committed。
