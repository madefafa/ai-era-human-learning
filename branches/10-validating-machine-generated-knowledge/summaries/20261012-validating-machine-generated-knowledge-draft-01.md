---
project_id: "ai-era-human-learning"
branch_id: "validating-machine-generated-knowledge"
branch_number: 10
summary_id: "20261012-validating-machine-generated-knowledge-draft-01"
operation_id: "op-ai-machine-knowledge-validation-draft-20261012-01"
parent_operation_id: "op-ai-machine-knowledge-validation-search-20261012-01"
status: draft
review_status: awaiting-confirmation
confirmed: false
generated_at: "2026-10-12T08:12:40Z"
---

# Issue 10 draft：AI 生成知识的可信度与验证

> 状态：`draft / awaiting-confirmation`，`confirmed=false`。本稿为候选简报，不是最终结论。所有外部材料均为 **搜索摘要级候选、未全文核验**。全文 **不预设 AI 已发现超越人类理解的新知识**。

## 1. 问题与目标

- 研究问题：面对机器提出的新概念和新结论，人如何判断、验证或继续研究？
- 目标：形成机器知识的证据分级与验证原则，覆盖来源追踪、可重复推导、独立验证、反例搜索、专家审查、实验与现实反馈。
- 本稿定位：基于一次已授权 webgo 检索（4 查询）与 10 张候选证据卡，组织验证节点与判断流程的**候选骨架**。

## 2. 已确认事实（项目内约定，非外部证据）

- branch `validating-machine-generated-knowledge`、`branch_number=10`；`current_branch` 保持该 branch；本次不处理 Issue 11–13，不修改 Issue 1–9。
- 检索 operation_id `op-ai-machine-knowledge-validation-search-20261012-01`，parent `op-ai-learning-20261012-26`；draft operation_id `op-ai-machine-knowledge-validation-draft-20261012-01`。
- webgo batch：`exit_code=0`，4/4 success，failed=0，retry=0；返回规模 `167/179/182/156`（合计 684，**非证据数**）；均 `target_reached`、1 页；`duplicates_removed=2/2/0/3`；失败引擎未报告。

## 3. 证据与来源（候选，10 张卡）

| # | 文件 | 节点 | support | confidence | 来源层级 |
|---:|---|---|---|---|---|
| 01 | [01-inspectable-ai-provenance-20261012](../evidence/01-inspectable-ai-provenance-20261012.md) | 来源追踪/溯源治理 | supports | medium | 预印本 |
| 02 | [02-rockgpt-curated-provenance-20261012](../evidence/02-rockgpt-curated-provenance-20261012.md) | 来源追踪 + 专家策展 | supports | medium | 期刊 |
| 03 | [03-reproducibility-ai-ml-definitions-20261012](../evidence/03-reproducibility-ai-ml-definitions-20261012.md) | 可重复推导/独立复现定义 | supports | medium | 期刊 |
| 04 | [04-falsifiable-replicable-ml-design-20261012](../evidence/04-falsifiable-replicable-ml-design-20261012.md) | 可证伪/可复制设计原则 | supports | medium | 预印本 |
| 05 | [05-llm-factuality-hallucination-survey-20261012](../evidence/05-llm-factuality-hallucination-survey-20261012.md) | 事实性/幻觉 + 人工标注 | contextual | medium | 期刊综述 |
| 06 | [06-accuracy-eval-incentivizes-hallucination-reduction-20261012](../evidence/06-accuracy-eval-incentivizes-hallucination-reduction-20261012.md) | 评估标准与幻觉抑制 | supports | low | 期刊（摘要少） |
| 07 | [07-machine-hypothesis-validation-survey-20261012](../evidence/07-machine-hypothesis-validation-survey-20261012.md) | 机器假设生成与验证 | contextual | medium | 预印本 |
| 08 | [08-co-scientist-independent-validation-20261012](../evidence/08-co-scientist-independent-validation-20261012.md) | 实验验证 + 独立复核 | supports | medium | 期刊 |
| 09 | [09-agentic-sequential-falsification-20261012](../evidence/09-agentic-sequential-falsification-20261012.md) | 反例搜索/证伪 | contextual | low | 预印本 |
| 10 | [10-epistemic-trust-calibration-tai-e-20261012](../evidence/10-epistemic-trust-calibration-tai-e-20261012.md) | 不确定性校准 + 来源归因 | supports | medium | 期刊 |

统计：supports=7、contextual=3、insufficient=0；confidence：medium=8、low=2。均为摘要级候选。

## 4. 机器主张的证据分级（候选框架，推论）

将机器生成知识视为**主张单元**，按“主张粒度”而非来源热度分级（以下为待验证的工作假设，不臆测具体样本/效应量）：

- **来源可追溯性**：能否定位支持陈述的原始文献/数据与检索过程（卡 01、02）。
- **推导可重复性**：中间步骤能否被独立重放/重实现，而非仅复述结论（卡 03、04）。
- **独立性**：验证者是否独立于原始生成系统与原始数据（卡 03、08）。
- **反例压力**：是否主动搜索反例/证伪而非只做确认（卡 09）。
- **现实表现**：是否经实验或现实反馈检验（卡 07、08）。
- **校准与来源归因**：主张是否随不确定性表达和来源标注呈现（卡 05、06、10）。
- **专家审查**：领域专家是否复核（卡 02）。

## 5. 验证流程（候选，推论）

1. 捕获主张与粒度（概念/规律/结论）。
2. 溯源：定位来源与检索过程（卡 01、02）。
3. 复现/独立重实现：核对推导链条（卡 03、04）。
4. 反例搜索与证伪尝试（卡 09）。
5. 独立复制与实验/现实反馈（卡 07、08）。
6. 校准与来源标注评估（卡 05、06、10）。
7. 专家审查与决策（采用 / 暂缓 / 拒绝 / 继续研究）。

该排序**并非既定标准**，各节点权重与顺序尚未验证。

## 6. 可重复推导

- 卡 03 给出可复现性的分层理解，含“独立复现”（不依赖原代码与数据）；卡 04 强调“主体间性”支持不同研究者独立复现。两者支持“验证需要可重复推导”的方向，但**术语体系可能不完全一致**（冲突/待统一）。
- 未核验：这些原则是否被实际采纳、采纳是否提升可靠性，及其成本。

## 7. 反例搜索

- 卡 09 提出代理式序贯证伪以验证难直接验证的抽象假设；这可作为“主动寻找反例”的候选机制。
- 证据极弱（预印本、摘要信息少、confidence=low）；不能据此认为自动化证伪可靠或充分。

## 8. 独立复制与实验/现实反馈

- 卡 08 描述机器生成假设经严格实验验证并涉及独立体外实验的案例，支持“生成—实验验证—独立复核”链条在具体案例中被实践。
- 卡 07 综述机器假设生成与验证框架，提供背景。
- 均未核验具体设计、成功率、负结果或泛化边界；**不得把单案例升级为通用结论**，也不得据此断言 AI 已发现超越人类理解的新知识。

## 9. 不可验证 / 证据不足

- 当前 10 张卡均为摘要级候选，**无一张经全文核验**；证据强度不足以支撑任何“机器生成知识普遍可信/普遍不可信”的判断。
- 缺少直接材料回答：不同领域（科学/工程/教育/社会）的最低验证门槛、验证成本与时效、黑箱模型的可解释边界、以及验证失败后的处置。
- 因此本稿对“机器主张是否已被独立验证”的答案保持为 **未知 / 证据不足**，不以流畅叙述代替证据等级。

## 10. 人与 AI 的认识论分工（候选，推论）

- 来源/推导的机器侧可支持：把生成陈述链接到来源、暴露溯源元数据（卡 01、02）。
- 人侧重在：判断来源合法性、设定反例与证伪策略、做独立复核与专家审查、承担采用/拒绝决策与责任（结合卡 10 的信任校准视角）。
- 该分工是**候选论证骨架**，权重与责任边界尚未确定；与 Issue 9 的人机分工、Issue 12 的主体性存在交叉，须保持独立处理。

## 11. 条件式未来边界（非事实）

- 若未来机器生成知识持续增长且新颖性提高，验证负担可能上升；这是一个 **条件式情景**（if-then），不是预测或既定事实。
- 本稿不主张 AI 已发现超越人类理解的新知识；是否出现及人类能否理解，属未决问题。

## 12. 反方与限制

- 反方一：把机器生成内容链接到来源/暴露溯源并不等于内容正确；可追溯性可能与正确性分离（卡 01、02 未提供正确性证据）。
- 反方二：自动化验证/证伪（卡 09）与模型自评可能被基准与评分标准塑造（卡 06 提示评估会激励特定行为），存在“评价即干预”的风险。
- 反方三：认识论信任量表测量的是“信任/来源归因”，**不等于测量知识正确性**（卡 10）。
- 限制：全部为摘要级候选；跨查询/跨卡重复（Query 1 与 Query 3 的复现/设计原则条目）尚未人工去重；术语不一致（可复现/可复制）尚未统一；未核验样本、方法、效应量与因果。

## 13. 下一步

1. 逐卡打开来源，核对出版状态、研究设计、任务/样本与结果；升级或降级 confidence。
2. 人工处理跨查询重复与冲突，为“可复现/可复制/独立复现”统一术语。
3. 将证据分级节点操作化：定义各节点的最低证据门槛、验证成本与风险。
4. 补充直接材料：不同领域验证门槛差异、验证失败处置、黑箱可解释边界。
5. 在本 branch 上按需发起后续 ask/search/summary（须另行明确授权）。
6. 与 Issue 9 / Issue 12 的边界交叉在各自 branch 内独立推进，不做跨 branch 合并。

## 14. 状态与生成时间

- summary 状态：`draft / awaiting-confirmation`；`confirmed=false`。
- 生成时间：`2026-10-12T08:12:40Z`；`current_branch=validating-machine-generated-knowledge`（未改变）。
- 证据边界：全部为摘要级候选，未全文核验；本稿不把搜索摘要升级为事实或因果，不预设 AI 已发现超越人类理解的新知识。
