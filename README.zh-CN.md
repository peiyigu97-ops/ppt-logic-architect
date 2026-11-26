# PPT Logic Architect 中文使用指南

**在打开任何 PPT 软件之前，先把演示文稿的逻辑设计好的 Agent Skill。**

你给它零散笔记、数据、论文，或一份已有的 PPT。它会提取真正已知的信息，建立中心论点和论证树，设计带有明确推进关系的章节顺序，逐页写出每一页的作用，最后对整体做逻辑审查。每个阶段结束都会停下来等你确认。它**不生成幻灯片**。

English: see [README.md](README.md).

> **版本状态：v0.1.0。** 已通过静态校验（目录结构、Frontmatter、引用路径）。`evals/` 里的行为测试用例已写好，但本版本尚未在真实 Agent 上跑过。详见文末"已知限制"。

## 它解决什么问题

多数 PPT 的问题不在排版，而在论证：中心论点只是个话题；章节顺序照搬笔记的顺序；结论比数据说得更满；没人说得清第 14 页为什么存在。改排版解决不了这些。

这个 Skill 处理排版之前的事：

- 这份 PPT 到底在主张什么？你手上的证据撑得住吗？
- 听众必须按什么顺序听，每一步为什么必须接在上一步之后？
- 哪些页在承担论证，哪些在重复，哪些什么都没做？

## 与普通 PPT 生成工具的区别

| | 普通 PPT 生成工具 | PPT Logic Architect |
|---|---|---|
| 产出 | `.pptx` 文件、排好版的页面 | Markdown 架构文档：论点、逻辑树、逐页卡片、证据矩阵、审查报告 |
| 起点 | 一个主题或提示词 | 你的原始资料，并区分事实、数据、他人主张、假设、待验证问题 |
| 标题 | 常是主题标签 | 完整的观点句，并配对应证据 |
| 证据 | 为了看起来完整而补上 | 绝不编造，缺失的证据记为"证据缺口" |
| 已有 PPT | 换皮肤 | 审查或重构，原稿每一页都有去向 |
| 控制 | 一步到位 | 六个阶段，每阶段等你确认 |
| 方法论 | 一套模板套所有 | 按目的和受众选择，并说明为什么选、为什么不选 |

它的定位是**上游**：负责逻辑，不负责画图。需要图表和幻灯片时，可以和 visual-explainer 搭配，见下文"与 visual-explainer 搭配"。

## 三种模式

| 模式 | 适用场景 | 产出 |
|---|---|---|
| **CREATE（创建）** | 有零散资料，还没有 PPT | 分阶段建立完整架构 |
| **RESTRUCTURE（重构）** | 已有 PPT 或大纲，但逻辑混乱 | 新结构，加上**每一页**原稿到新页的映射表 |
| **AUDIT（审查）** | 只想要审查，不想被改写 | Critical / Major / Minor 分级问题，每条含位置、原因、影响、修改方向 |

## 六个阶段

| 阶段 | 名称 | 结束时产出 |
|---|---|---|
| 1 | Intake & Diagnosis（资料诊断） | 资料登记、分类证据、需求简报、早期缺口 |
| 2 | Thesis & Argument Architecture（论点与论证） | 限定范围的中心论点、方法选择、逻辑树 |
| 3 | Section Architecture（章节架构） | 章节顺序、章节间明确的推进关系 |
| 4 | Slide-by-Slide Architecture（逐页架构） | 每页一张完整卡片 |
| 5 | Logic Audit（逻辑审查） | 问题清单，并在源头修复 |
| 6 | Final Architecture Delivery（最终交付） | 五个 Markdown 文件 |

每个阶段结尾都有确认节点：本阶段目标、结果、未解决问题（标 `BLOCKING` 或 `CAN PROCEED`）、至多三个待你决定的事项（附推荐默认值）、下一步。Agent 会停下等你。你可以跳过已经做完的阶段、返回修改之前的阶段，也可以一次要求跑多个阶段（只在最后设一个确认点）。

## 逐页卡片包含什么

每页必须包含十个字段：页码、所属章节、观点型标题、核心信息、支撑证据、存在理由、与上一页的逻辑关系、向下一页的过渡、建议视觉形式、证据来源与置信度。只有标题加几个关键词不算卡片。

输出内容会使用你的语言，但字段名保持英文（如 `Action-oriented Headline`），方便统一检查。

## 方法论

按需加载，不会一次性全读：

- **金字塔原理**：自上而下的论证、纵向与横向逻辑
- **SCQA**：情境、冲突、疑问、回答；只在确实存在冲突时使用
- **Assertion-Evidence**：观点型标题加证据支撑
- **MECE**：仅用于真正的"划分"，否则如实写成"有明确标准的逻辑分组"
- **循证推理**：主张 / 证据 / 依据；事实与推论的区分；来源追踪；证据缺口
- **逻辑审查**：论证有效性、因果、过渡、重复、矛盾、缺失环节
- **设计研究与工程推理**：从研究问题到验证的完整链条，含八项检查

另有一份方法选择指南，决定哪些方法适用。本 Skill 明确不会把 MECE 硬套在天然交叉的想法上，也不会把 SCQA 硬套给已经了解背景的听众。

### 工业设计与技术研究模块

适用于工业设计、交互设计、产品服务系统、硬件原型、HCI 研究、工程研究、作品集和答辩。检查这条链：研究问题、研究方法、研究发现、用户洞察、设计要求、概念发展、技术可行性、原型、测试、迭代、最终方案、验证。重点八问：

1. 研究发现是否真的支持洞察？
2. 洞察是否能转化为具体设计要求？
3. 设计要求是否能解释方案选择？
4. 技术路线是否有可行性依据？
5. 原型是否验证了关键假设？
6. 测试结果是否支持最终结论？
7. 是否从研究直接跳到了造型？
8. 是否把未经验证的设计假设当成了研究结论？

## 安装

需要的只是 `skills/ppt-logic-architect/` 这个文件夹。它是纯 Markdown，没有脚本、不联网、不依赖任何包。

```bash
git clone <仓库地址> ppt-logic-architect
cd ppt-logic-architect

./install/install.sh --target claude          # Claude Code: ~/.claude/skills/
./install/install.sh --target codex           # Codex: ${CODEX_HOME:-~/.codex}/skills/
./install/install.sh --target all --dry-run   # 先预览，不改动任何文件
```

也可以手动复制：把 `skills/ppt-logic-architect/` 放进 Agent 的 skills 目录，使 `SKILL.md` 位于 `<skills目录>/ppt-logic-architect/SKILL.md`。文件夹名必须与 skill 名一致。

安装后请**新开一个会话**，Agent 才会重新扫描技能。路径验证细节见 [install/install-claude-code.md](install/install-claude-code.md) 和 [install/install-codex.md](install/install-codex.md)。

**Windows 没有 Git Bash / WSL 时**：用资源管理器或 PowerShell 手动复制文件夹，两份安装指南里都有命令。

## 在 Claude Code 中使用

直接用自然语言，或点名 Skill：

```text
用 ppt-logic-architect 把 ./research/ 里的笔记整理成演示文稿结构。
用 ppt-logic-architect 重构 deck-outline.md，有用的内容都要保留。
用 ppt-logic-architect 的 AUDIT 模式审查 thesis-defense.pptx，不要改写。
```

部分版本的 Claude Code 可能也会把已安装的技能暴露为 `/ppt-logic-architect` 命令，本 Skill 尚未验证这一点。

## 在 Codex 中使用

```text
$ppt-logic-architect  把 ./research/ 里的笔记整理成演示文稿结构。
用 $ppt-logic-architect 审查 slides.md 的逻辑，不要改写。
```

Codex 也会根据描述自动选择技能，所以"帮我检查答辩 PPT 的逻辑"这类请求不点名也可能触发。

## 如何触发三种模式

Skill 会根据你的请求判断模式，并说明选了哪个。想强制指定就直接说：

| 模式 | 会路由到它的说法 |
|---|---|
| CREATE | "根据这些笔记做 PPT 大纲"、"把研究整理成叙事线"、"规划每一页" |
| RESTRUCTURE | "重构这份 PPT"、"理顺结构"、"重新组织章节"、"有用的都保留" |
| AUDIT | "审查"、"检查逻辑"、"论证站得住吗"、"找问题"、"不要改写" |

如果分不清你要重构还是审查，它默认走 AUDIT（不改动任何内容），并在结束后提议是否继续重构。

## 会生成什么文件

第 6 阶段写出五个文件，默认放在 `./ppt-architecture/`，不会在未询问时覆盖已有文件：

| 文件 | 内容 |
|---|---|
| `master-outline.md` | 简报、论点、方法选择、章节、推进关系、标题链、决策记录 |
| `logic-tree.md` | 带证据链接的论证树、依据和可能的质疑 |
| `slide-by-slide.md` | 每页卡片；重构模式下含新旧页面映射 |
| `evidence-matrix.md` | 来源、证据条目、主张与证据对照、假设、缺口 |
| `logic-audit-report.md` | 按严重程度分级的问题及处理结果 |

## 与 visual-explainer 搭配（可选）

本 Skill 只设计逻辑，不画图。[visual-explainer](https://github.com/nicobailon/visual-explainer)（MIT 许可，作者 nicobailon）负责画：以图为主的 HTML 页面、逻辑图和幻灯片。这样分工能守住证据底线：本 Skill 决定"主张什么、证据有多强"，visual-explainer 照着画出来。

第 6 阶段之后，**只有你提出要求时**，Skill 才会根据已确认的卡片写出 `visual-brief.md`，再交给 visual-explainer：

```text
（完成第 6 阶段并确认架构）
现在把确认后的架构做成逻辑树图和可视化幻灯片。
```

| 我们的文件 | 变成 |
|---|---|
| `logic-tree.md` | 论证树图页面，带置信度标记，证据缺口用虚线节点 |
| `slide-by-slide.md` | HTML 幻灯片，每张卡片一页 |
| `logic-audit-report.md` | 审查页：结论、证据图、风险、下一步 |
| `evidence-matrix.md` | 带状态标记的表格 |

交接时遵守的规则（详见 [`references/visual-handoff.md`](skills/ppt-logic-architect/references/visual-handoff.md)）：图里不得出现新数字或新主张；标题逐字照抄；每张卡片都成为一页；Low / None 置信度和未解决的缺口在图中必须可见；生成结果要回头对照简报检查。

**你必须知道的限制：**

- **导出 PPTX 会丢掉图。** visual-explainer 自己的文档写明，`--pptx` 导出是"尽力而为"的静态转换，会丢掉 SVG、图表和图注。真正的成品是 HTML 幻灯片，PPTX 只是文字和表格的交接版本。
- **两个 Skill 都不能原地修改已有的 `.pptx`。** 对你已有的 PPT，RESTRUCTURE 模式会给出每一页"旧页到新页"的映射表，再由人或其他工具去改文件。
- **尚未端到端运行。** 命令和图表类型是对照 visual-explainer v0.16.0 的文档核对的，没有把两个 Skill 真正跑通过。对应测试用例是 TC9。
- 没装 visual-explainer 时，Skill 会如实说明，并停在简报这一步。安装步骤见两份安装指南。

两个完整示例（数据均为虚构）在 [`skills/ppt-logic-architect/examples/`](skills/ppt-logic-architect/examples/)：技术研究进展汇报，以及工业设计评审答辩。

## 如何扩展方法论

1. 新建 `skills/ppt-logic-architect/references/<方法名>.md`：它是什么、何时适用、**何时不适用**、如何应用、常见陷阱。
2. 在 `references/method-selection.md` 中登记。
3. 在 `SKILL.md` 的"Which references to load"表里加一行。
4. 在 `evals/test-cases.md` 加一个没有它就会失败的测试用例。

新增项目类型模块（如临床研究、法律论证）可参照 `references/design-research-reasoning.md`。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 测试

分为两层，刻意分开：

- **静态检查**（`python scripts/validate.py`）：Frontmatter 字段与长度、目录名等于 skill 名、所有相对引用可解析、十个卡片字段齐全、示例完整且声明为虚构。它只证明包的结构没问题，**不证明行为正确**。
- **行为测试**（[`evals/test-cases.md`](evals/test-cases.md)）：九个带"埋入缺陷"的用例，覆盖：数字互相矛盾的零散笔记、含重复页的混乱 PPT、从研究直接跳到造型的设计项目、落在仪器误差内的技术结果、结论超出证据、重复与无效页面、阶段确认与跳转处理、被要求编造数据时的表现、可视化交接。每个用例有可观察的"必须 / 不得"条目，答案和评分规则见 [`evals/expected-behavior.md`](evals/expected-behavior.md)。

## 已知限制

- 行为测试用例已写好，但本版本**尚未在真实 Agent 上运行**。请把最初几次使用当作验证的一部分，并反馈失败案例。
- 输出质量取决于底层模型能否遵循较长的指令。较弱的模型可能跳过确认节点或把问题说轻，测试用例正是为暴露这类情况设计的。
- 它处理的是结构和证据。它无法核实某个来源是否真实、某个数字是否正确，读不了的内容会明确说明。
- 它自己不画图、不生成幻灯片、不写演讲稿。视觉部分通过可选的 visual-explainer 交接完成，限制见上文。

## GitHub 仓库建议描述

**Description：** An Agent Skill that designs the logic of a presentation before any slides exist: thesis, argument tree, slide-by-slide architecture, and logic audit. For Claude Code, Codex, and other Agent Skills tools.

**中文简介：** 在做 PPT 之前先设计逻辑的 Agent Skill：中心论点、论证树、逐页架构、逻辑审查。兼容 Claude Code、Codex 及其他遵循 Agent Skills 规范的工具。

**Topics：** `agent-skills`、`claude-code`、`codex`、`presentation`、`pptx`、`storytelling`、`pyramid-principle`、`logic`、`design-research`、`ai-agents`

## 许可证

MIT，见 [LICENSE](LICENSE)。
