---
search_id: "20261012-understanding-validation-search-plan-01"
operation_id: "op-ai-understanding-validation-search-20261012-01"
project_id: "ai-era-human-learning"
branch_id: "validating-understanding"
branch_number: 7
status: awaiting-authorization
search_status: awaiting-authorization
created_at: "2026-10-12T14:09:55+08:00"
updated_at: "2026-10-12T14:09:55+08:00"
parent_operation_id: "op-ai-learning-20261012-20"
---

# Issue 7 检索计划

## 计划边界

- 目标 branch：`validating-understanding`（Issue 7）
- 研究问题：如何区分熟悉感与真正掌握？
- 计划用途：为理解验证环节寻找候选研究来源；仅生成计划，等待负责人绑定本 operation_id 明确授权后执行。
- 脱敏说明：查询词不包含个人信息、内部路径、凭证、私密链接或不必要的原始上下文。
- 明确未执行：本文件创建时未调用 webgo，未获得本次检索授权，未创建 evidence 卡或 summary/draft。

## 查询参数

每项均使用：`itemnums=15`；`categories=science,general`。

| 序号 | query | 聚焦 | 预期产出 |
|---:|---|---|---|
| 1 | `delayed retrieval without aids recall reconstruction learning understanding` | 延迟无辅助回忆、核心模型重建与理解验证 | 候选研究：区分即时熟悉感与延迟独立提取/重建表现的任务、指标和限制 |
| 2 | `metacognitive calibration familiarity fluency illusion of knowing learning judgments` | 元认知校准、熟悉感与流畅性错觉 | 候选研究：学习判断与实际表现的偏差、校准方法及适用边界 |
| 3 | `prediction counterexample variation transfer tasks conceptual understanding learning` | 预测、反例、变式与迁移任务 | 候选研究：用预测失败、反例解释、变式问题和迁移任务检验模型理解的证据与局限 |
| 4 | `AI assisted performance withdrawal support independent learning transfer` | AI 辅助表现与撤除辅助后的独立能力 | 候选研究：辅助条件与无辅助条件的表现差异、撤除支架后的独立能力和评价设计 |

## 授权门禁

- 当前状态：`awaiting-authorization`。
- 负责人后续如确认执行，必须明确绑定：`确认执行 op-ai-understanding-validation-search-20261012-01`。
- 未收到绑定确认前，不得调用 webgo；不得把本计划视为检索结果或证据。
- 本计划不生成 `search-authorize` 决策；实际授权时才追加对应决策。

## 预期落盘范围

- 计划文件：本文件。
- 若未来获得授权，实际 search 结果仍只能写入本 Issue 7 的 `searches/`，并另行执行 evidence、summary 和项目同步流程。
- 本次未新增 evidence、summary/draft，也未修改 Issue 1–6 研究正文或处理 Issue 8–13。
