---
search_id: "20261011-ai-knowledge-functions-search-01"
operation_id: "op-ai-knowledge-functions-search-20261011-01"
parent_operation_id: "op-ai-learning-20261011-09"
project_id: "ai-era-human-learning"
branch_id: "functions-of-knowledge"
branch_number: 2
status: completed
retrieved_at: "2026-10-11T15:18:48Z"
actor: "user + idea-navigator + webgo"
itemnums: 15
categories: "science,general"
requested_count: 4
completed_count: 4
failed_count: 0
success_rate: 1.0
failure_rate: 0.0
retry_count: 0
elapsed_seconds: 60.09151245799876
---

# 检索范围

本次检索严格限定于 Issue 2 `functions-of-knowledge`，用于探索背景知识、认知框架、专家知觉、知识类型、理解/迁移以及判断/智慧之间的关系。查询已脱敏；不涉及 Issue 3–13，也未修改 Issue 1 内容。

## 查询与工具状态

| 序号 | query | status | returned_itemnums / item_count | diagnostics | 失败引擎/噪声 |
|---:|---|---|---:|---|---|
| 1 | `background knowledge cognitive schema comprehension problem representation` | success | 242 / 242 | stop_reason=target_reached; page_count=1; duplicates_removed=0 | 未报告失败引擎；含中文内容、词典、个人主页、ResearchGate、未来日期页面等噪声 |
| 2 | `knowledge expertise perception attention reasoning problem solving` | success | 260 / 260 | stop_reason=target_reached; page_count=1; duplicates_removed=1 | 未报告失败引擎；含商业健康/教育博客、Wikipedia、词典和明显无关结果 |
| 3 | `declarative procedural conceptual knowledge understanding transfer` | success | 226 / 226 | stop_reason=target_reached; page_count=1; duplicates_removed=2 | 未报告失败引擎；含 Wikipedia、Quizlet、商业博客、词典和跨领域/未来日期结果 |
| 4 | `knowledge judgment wisdom decision making education` | success | 269 / 269 | stop_reason=target_reached; page_count=1; duplicates_removed=0 | 未报告失败引擎；含商业推广、新闻评论、ResearchGate、无关天文教育结果 |

批次汇总：`exit_code=0`，`requested_count=4`，`completed_count=4`，`failed_count=0`，`success_rate=1.0`，`failure_rate=0.0`，`retry_count=0`。工具诊断显示四项均在一页达到目标停止条件。

## 返回规模解释

webgo 工具返回规模为 242、260、226、269；这些数字是检索候选项目返回规模，不是经过筛选、全文阅读、质量评价或独立复核后的证据数量，也不等同于 `itemnums=15` 张证据。本文只从 top_items 中挑选少量候选来源建立 evidence cards，所有卡片均保留摘要级边界。

## 候选来源摘要

### 查询 1：背景知识、图式与理解

候选包括：

- *The Role of Background Knowledge in Reading Comprehension: A Critical Review*，Taylor & Francis，摘要涉及背景知识与阅读理解模型的关系。
- *Schema Theory*，EBSCO Research Starters，摘要将 schema 描述为组织和整合新信息的认知框架。
- *Diagnostic Schemas: Form and Function*，PMC/NIH，摘要提到 schema 可将孤立知识组块化，并与临床问题解决相关。
- *Schema Theory – Design in Progress*，Pressbooks，摘要涉及激活相关既有图式与连接新信息。
- *Cognitive Processes in Reading Comprehension*，会议论文 PDF，摘要涉及激活和构建背景知识。

该查询也返回中文页面、个人主页、词典、ResearchGate、MIT 书目 PDF 和一篇未来日期 arXiv 页面。它们不是本轮事实结论的依据。

### 查询 2：知识、专家、知觉、注意与问题解决

候选包括：

- *Human intelligence and brain networks*，PMC/NIH，摘要将推理、问题解决和学习与知觉、注意、记忆、语言、计划等能力联系起来。
- *Cognitive psychology*，EBSCO Research Starters，摘要列出知觉、记忆、推理、问题解决、智能、语言和创造力等研究主题。
- *Cognitive Approach In Psychology*，Simply Psychology，摘要涉及记忆、知觉、注意、问题解决和推理。
- *A Computationally Grounded Logic of Visibility, Perception, and Knowledge*，KISTI/论文索引，标题指向可见性、知觉和知识的关系。

其余候选中有健康产品博客、词典、Wikipedia、无关生活意义网页和 ResearchGate 页面，不能直接支撑 Issue 2 的强主张。

### 查询 3：陈述性、程序性、概念性知识与迁移

候选包括：

- *Complex Declarative Learning*，Arizona State University PDF，摘要区分概念知识与陈述性知识，并将其与程序性知识对照。
- *Learning & Teaching Foreign Languages*，Université Côte d’Azur，摘要将关于语言形式的知识作为陈述性知识，将“如何做”作为程序性知识示例。
- *Procedural knowledge*，Wikipedia，摘要涉及概念性教学、概念理解、程序生成与迁移，但需回溯原始研究。
- *Technology-Supported Math Instruction for Students with Disabilities*，LD Online，摘要涉及陈述性、程序性和概念性知识的教学目的。
- *The Impact of Virtual Reality Immersion on Learning Outcomes*，MDPI，摘要涉及沉浸与陈述性/程序性知识获得之间的关系，但摘要不足以确认因果。

该查询同时返回 Quizlet、商业博客、词典和跨领域机器人论文，均只作为噪声或低置信上下文。

### 查询 4：知识、判断、智慧与教育

候选包括：

- *From Knowledge to Wisdom: Looking beyond the Knowledge Hierarchy*，MDPI，摘要明确将知识到智慧的转变与判断和决策联系起来，并讨论经验性学习。
- *A Polyhedron Model of Wisdom: A Systematic Review...*，DOI/OpenAlex，摘要指出智慧没有统一定义，并综述心理学、管理、领导与教育领域的研究。
- *Making good choices when life gets messy*，University of Tennessee，摘要区分理论知识、技术技能与情境判断（phronesis），但需核验正文与来源类型。
- *Why schools should teach for wisdom*，Taylor & Francis，摘要指出正式知识可能与明智判断和决策相关，而不是当然无关。
- *A Universal Theory of Wisdom*，DOI/OpenAlex，摘要将智慧描述为基于知识的判断的综合理论，但需阅读全文核验。

该查询还返回商业推广页、新闻评论、LinkedIn、无关 NASA 教育项目和空摘要条目，不能作为强证据。

# 候选证据边界

- 本记录保存 webgo 的实际返回状态、规模和代表性候选；没有逐篇打开全文、核验方法、样本、效应量、发表日期或引用链。
- snippets 仅用于候选筛选，不能单独证明因果关系、普遍性、教育效果或“知识层级”的必然顺序。
- `supports` 只表示候选摘要与某个有限主张方向一致，不表示来源已完成质量审查。
- 结果噪声明显，但本批次没有工具层面的失败引擎或部分失败；失败引擎字段为“未报告”。

# 用户汇报摘要

本次 `op-ai-knowledge-functions-search-20261011-01` 已完成：webgo batch `exit_code=0`，4/4 查询成功，返回规模为 242、260、226、269，工具诊断未报告失败引擎，批次重试次数为 0。候选主题集中在背景知识/图式与理解、专家知识与问题表征、陈述性/程序性/概念性知识与迁移、知识与判断/智慧；同时含有明显噪声和低质量来源。返回数量不作为证据数量。已创建 8 张摘要级候选 evidence cards，均明确标注适用范围、局限和待全文核验状态；将基于这些卡片形成 `draft` summary，不标记为 confirmed。

# 操作日志

- operation_id: `op-ai-knowledge-functions-search-20261011-01`
- event_type: `search`
- authorization: `确认执行检索 op-ai-knowledge-functions-search-20261011-01`
- status: `completed`
- parent_operation_id: `op-ai-learning-20261011-09`
- scope: `Issue 2 / functions-of-knowledge only`
- not_executed: `Issue 3–13；Issue 1 内容修改；全文逐篇核验；最终结论确认`
