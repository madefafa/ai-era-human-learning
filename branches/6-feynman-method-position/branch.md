---
project_id: "ai-era-human-learning"
branch_id: "feynman-method-position"
branch_number: 6
name: "费曼解释法的真实位置"
status: draft
question: "费曼解释法是工具、指标，还是学习理论？"
objective: "评估解释暴露知识漏洞的价值及其边界，区分解释能力与实践能力，并比较练习、反馈、实验、讨论和检索练习等补充机制。"
priority: P2
search_status: completed
constraints:
  - "本轮只处理 Issue 6；不处理 Issue 7–13。"
  - "不修改 Issue 1–5；不创建其他 branch；不切换 current_branch。"
  - "摘要级结果按候选证据保守使用，费曼法不表述为唯一或充分方法。"
assumptions: []
evidence_count: 8
summary_count: 1
created_at: "2026-10-12T05:32:26Z"
updated_at: "2026-10-12T05:48:49Z"
operation_id: "op-ai-feynman-method-search-20261012-01"
last_operation_id: "op-ai-feynman-method-draft-20261012-01"
---

# 用户输入

- Issue 6：`feynman-method-position`
- branch_number：6
- branch_id：`feynman-method-position`
- name：费曼解释法的真实位置
- question：费曼解释法是工具、指标，还是学习理论？
- objective：评估解释暴露知识漏洞的价值及其边界，区分解释能力与实践能力，并比较练习、反馈、实验、讨论和检索练习等补充机制。
- 用户授权创建 branch 原文：`授权创建 branch op-ai-learning-20261012-17`
- 用户检索授权原文：`确认执行检索 op-ai-feynman-method-search-20261012-01`

# 已确认内容

- 本次完成 Issue 6 webgo—候选证据—draft 流程，检索 operation_id=`op-ai-feynman-method-search-20261012-01`，draft operation_id=`op-ai-feynman-method-draft-20261012-01`。
- 当前 project current_branch 仍为 `feynman-method-position`；未执行切换操作。
- Draft 状态为 `draft/awaiting-confirmation`，未标记 confirmed。
- 8 张卡是候选证据：摘要级结果均说明来源边界和待全文核验事项，不等于 8 项已完成质量评估的确定证据。

# 待确认问题

- 用户是否确认该 draft 的方法定位和章节论证结构，尚待确认；未收到确认前不得改为 confirmed。

# 模型推论

- 当前暂定定位是自我解释/检索活动的学习脚手架，可帮助组织知识和暴露缺口，但不能单独证明实践能力、远迁移或完整学习理论。
- 该判断为基于候选摘要形成的低置信度综合，须经原文核验和系统化补充检索修订。

# 检索记录

- `20261012-feynman-method-search-01`：completed；2026-10-12T05:41:30Z；4 个查询，每项 `itemnums=15`、`categories=science,general`；batch `exit_code=0`，4/4 success、0 failed、0 retry；候选规模 206/202/202/175（总 785，不等于证据数量）；记录见 [`searches/20261012-feynman-method-search-01.md`](searches/20261012-feynman-method-search-01.md)。
- operation_id：`op-ai-feynman-method-search-20261012-01`；parent_operation_id：`op-ai-learning-20261012-18`。

# 证据索引

| evidence_id | 主张/范围 | 来源 | 状态 | 相对路径 |
|---|---|---|---|---|
| bisra-self-explanation-meta-analysis-20261012 | 自我解释元分析；限于受研究任务 | Inducing self-explanation: A meta-analysis | supports / medium | `evidence/bisra-self-explanation-meta-analysis-20261012.md` |
| math-self-explanation-meta-analysis-2017 | 数学自我解释与知识/迁移；题录摘要待核 | Promoting self-explanation to improve mathematics learning | contextual / low | `evidence/math-self-explanation-meta-analysis-2017.md` |
| feynman-technique-direct-evidence-gap-20261012 | 完整命名流程直接证据不足；不是无效证明 | Innovation Training 指南搜索摘要 | insufficient / low | `evidence/feynman-technique-direct-evidence-gap-20261012.md` |
| self-explanation-critical-thinking-transfer-2018 | 任务依赖及零/负向摘要线索 | Frontiers 2018 | contextual / low | `evidence/self-explanation-critical-thinking-transfer-2018.md` |
| self-explanation-practice-transfer-study-2010 | 迁移/教学组合研究问题；结果未确认 | Promoting Transfer PDF 候选 | contextual / low | `evidence/self-explanation-practice-transfer-study-2010.md` |
| retrieval-practice-worked-examples-goals-2018 | 策略优势与学习目标相关 | Retrieval Practice Versus Worked Examples | contextual / low | `evidence/retrieval-practice-worked-examples-goals-2018.md` |
| retrieval-practice-stepwise-worked-examples-2025 | 低检索成功率、反馈条件可能重要 | Retrieval Practice in Stepwise Worked Examples Improves Learning | contextual / low | `evidence/retrieval-practice-stepwise-worked-examples-2025.md` |
| self-explanation-feedback-learning-study-2024 | 标准提示与支架设计边界 | Effects of self-explaining feedback on learning from problem-solving | contextual / low | `evidence/self-explanation-feedback-learning-study-2024.md` |

计数：evidence_count=8，与 evidence 文件数一致；summary_count=1，与本 branch draft 文件数一致。

# branch 询问记录

- 暂无独立 ask 操作。

# summary 索引

- `20261012-feynman-method-position-draft-01`：`draft/awaiting-confirmation`；operation_id=`op-ai-feynman-method-draft-20261012-01`；父操作=`op-ai-feynman-method-search-20261012-01`；[`summaries/20261012-feynman-method-position-draft-01.md`](summaries/20261012-feynman-method-position-draft-01.md)。未 confirmed。

# 未解决事项

- 核验自我解释元分析的全文、纳入标准、效应量、异质性、偏倚及调节变量。
- 核验数学元分析以及所有摘要级研究的出版题录、样本、任务和研究设计。
- 对命名费曼技巧完整流程进行系统检索，确认是否有直接对照研究；目前只能说本次检索未确认。
- 区分解释表现、近迁移、远迁移、延迟保持与真实操作能力；评估解释流畅/简化造成误解的风险。
- 核对摘要中的零/负向或反馈依赖线索，判断与元分析总体结果是否因任务和设计差异而可并存。
- 检验初学者先备知识、任务复杂度和反馈质量对方法收益的调节。
- 用户尚未确认 draft；状态保持 `draft/awaiting-confirmation`。

# 操作日志

## 2026-10-12T05:41:30Z — search

- operation_id：`op-ai-feynman-method-search-20261012-01`
- parent_operation_id：`op-ai-learning-20261012-18`
- actor：`user + idea-navigator + webgo`
- status：`committed`
- event_type：`search`
- authorization：`确认执行检索 op-ai-feynman-method-search-20261012-01`
- result：batch `exit_code=0`，requested/completed/failed=`4/4/0`，retry=0；候选规模 206/202/202/175；均单页 `target_reached`；duplicates_removed=3/1/1/2；失败引擎未报告。
- affected_paths：search 记录、8 张 evidence 卡、本文件、project.md、decisions.md、MEMORY.md。
- noise：博客/商业指南、论坛、词典/百科、无关网页、摘要截断和日期/质量待核条目。
- validation：候选数量未误计为证据数；仅作用于 Issue 6；current_branch 不变。

## 2026-10-12T05:48:49Z — draft

- operation_id：`op-ai-feynman-method-draft-20261012-01`
- parent_operation_id：`op-ai-feynman-method-search-20261012-01`
- actor：`idea-navigator`
- status：`awaiting-confirmation`
- event_type：`summary-draft`
- affected_paths：本 draft、branch.md、project.md、decisions.md、MEMORY.md。
- result：生成覆盖方法定位、机制假设、效果边界、解释/实践差异、其他方法关系、反方限制、证据边界和下一步的工作稿。
- validation：保留未知与摘要级局限；draft 未标记 confirmed。

## 2026-10-12T05:48:49Z — branch-boundary-validation

- operation_id：`op-ai-feynman-method-draft-20261012-01`
- parent_operation_id：`op-ai-feynman-method-search-20261012-01`
- status：`committed`
- validation：仅新增 Issue 6 检索、证据卡、draft 和项目/审计摘要；没有处理 Issue 7–13，没有修改 Issue 1–5，没有创建其他 branch，没有切换 current_branch。
