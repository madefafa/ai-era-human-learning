# 项目恢复锚点

- 项目：`ai-era-human-learning`
- 当前 branch：`human-ai-robot-future-boundaries`（Issue 13，branch_number=13）；本次未切换。
- Issue 1–12 研究正文：本次未修改。
- Issue 13 检索 operation：`op-ai-future-boundaries-search-20261012-01`，parent=`op-ai-learning-20261012-32`，batch exit_code=0，4/4 success，返回规模 157/152/156/107，总计 572；无失败引擎、无重试；去重分别 1/0/0/0。
- Issue 13 draft operation：`op-ai-future-boundaries-draft-20261012-01`，parent=`op-ai-future-boundaries-search-20261012-01`，状态 `draft/awaiting-confirmation`，`confirmed=false`。
- 已落盘：
  - `branches/13-human-ai-robot-future-boundaries/searches/20261012-future-boundaries-search-01.md`
  - `branches/13-human-ai-robot-future-boundaries/evidence/` 下 10 张候选卡（E01–E10）
  - `branches/13-human-ai-robot-future-boundaries/summaries/20261012-human-ai-robot-future-boundaries-draft-01.md`
- 证据边界：以 snippet 级保守标注；support/contextual/insufficient 与 confidence、范围、局限均已记录；未来情景和超级智能未写成事实。
- 待完成同步：branch.md、project.md、decisions.md；完成后做 current_branch、产物计数、operation_id、Issue1–12 边界校验。
- 恢复规则：先检查上述文件和 operation_id，避免重复创建；不得创建其他 branch；不得覆盖既有 Issue 1–12 正文。
