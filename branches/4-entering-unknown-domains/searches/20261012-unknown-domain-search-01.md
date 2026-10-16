---
search_id: "20261012-unknown-domain-search-01"
operation_id: "op-ai-unknown-domain-search-20261012-01"
parent_operation_id: "op-ai-learning-20261011-14"
branch_id: "entering-unknown-domains"
status: completed
occurred_at: "2026-10-12T12:38:20+08:00"
retrieved_at: "2026-10-12T12:38:20+08:00"
recorded_at: "2026-10-12T12:38:20+08:00"
actor: "user + idea-navigator + webgo"
itemnums: 15
categories: "science,general"
query_count: 4
---

# 检索范围

本次只服务 Issue 4 `entering-unknown-domains`，不处理 Issue 5–13，不修改 Issue 1–3，不创建或切换 branch。用户授权原文：`确认执行检索 op-ai-unknown-domain-search-20261012-01`。

## 查询与实际状态

| # | query | status | returned_itemnums / item_count | stop_reason | page_count | duplicates_removed |
|---:|---|---|---:|---|---:|---:|
| 1 | `novice learning unfamiliar domain concept map terminology prior knowledge` | success | 216 / 216 | target_reached | 1 | 2 |
| 2 | `expertise reversal effect scaffolding cognitive load novice learning` | success | 142 / 142 | target_reached | 1 | 3 |
| 3 | `metacognition illusion of understanding self explanation knowledge monitoring` | success | 186 / 186 | target_reached | 1 | 3 |
| 4 | `AI assisted learning unfamiliar domain hallucination verification` | success | 201 / 201 | target_reached | 1 | 2 |

> 返回规模是 webgo 候选结果规模，不是证据数量，也不是全文核验数量。

## Webgo 总体诊断

- `exit_code: 0`
- `requested_count: 4`
- `completed_count: 4`
- `failed_count: 0`
- `success_rate: 1.0`
- `failure_rate: 0.0`
- `retry_count: 0`
- `elapsed_seconds: 34.87120645899995`
- 4 项均为 `success`，均 `target_reached`，每项 1 页。
- 返回中存在重复合并：2、3、3、2 条。
- 失败引擎：webgo 未报告失败引擎；不能据此推断所有引擎均无异常。

## 噪声与候选来源边界

结果混有论文/医学数据库、出版社页面、机构教学材料、预印本、博客、论坛/商业页、词典、Wikipedia、多语言搜索结果及明显未来日期条目。部分标题与 snippets 只提供方向性线索，不能替代全文核验。尤其是 AI 辅助学习查询中，hallucination、验证和陌生领域学习的直接实证关系仍较稀疏；“novice verification problem”等较新的候选不作为已确立术语。

## 候选来源摘要（未全文核验）

1. **陌生领域、先验知识、概念地图**：PMC 预训练/认知负荷候选、IHMC concept maps 理论页、PLOS ONE 概念图研究、Springer 概念图综述页、北京师范大学中文研究结果。方向性提示：先验知识可能影响陌生概念连接；概念图/术语表可作为入口组织工具，但具体效果依赖任务、学习者和地图形式。
2. **认知负荷与脚手架**：Springer expertise reversal effect 论文页及多条教学解释页。方向性提示：面向新手的详细支持可能有帮助；随着知识增加，冗余指导可能变成负担。需全文核验研究条件和效应边界。
3. **元认知与理解错觉**：PMC `The Illusion of Knowing in Metacognitive Monitoring`、Springer metacognitive illusion、大学教学材料及相关综述候选。方向性提示：主观熟悉/流畅感不能自动证明可解释、可提取或可迁移。
4. **AI 辅助与验证**：IEEE Computer Society hallucination 解释页、IBM hallucination 页、AI 学习候选论文/系统综述和预印本。方向性提示：生成流畅与事实核验不同；高风险或陌生领域使用需要外部来源、交叉核对和人类责任。但 AI 对陌生领域学习成效的因果证据尚不足。

## 用户汇报摘要

- 实际检索状态：`exit_code=0`，4/4 成功，失败 0，重试 0。
- 实际返回规模：216、142、186、201；这些数字只是候选返回规模，不计作证据数量。
- 主要候选方向：先验知识与概念地图、认知负荷/脚手架的阶段适配、元认知理解错觉、AI 生成内容的幻觉风险与验证边界。
- 诊断：4 项均 `target_reached`、`page_count=1`；webgo 未报告失败引擎；结果含重复合并和明显噪声，需保守筛选。
- 证据边界：本记录基于搜索结果标题与摘要级信息；候选来源尚未逐篇全文核验，不把 snippets 写成完成核验的事实。
- 落盘状态：本检索记录已写入；后续将在同一检索操作下创建 8 张候选 evidence cards，并生成独立 draft 操作；summary 只能保持 `draft/awaiting-confirmation`，不得标记 `confirmed`。

## 待执行与未解决

- [x] 检索记录及用户汇报摘要落盘。
- [ ] 建立 6–10 张候选 evidence cards；逐卡保留 support/contextual/insufficient、confidence、范围与局限。
- [ ] 基于候选卡生成 Issue 4 draft summary。
- [ ] 对高影响主张进行全文核验、来源去重和研究条件核对（需后续独立授权）。
- [ ] 进一步区分“地图构建工具有效”与“地图本身等于理解”的主张。
