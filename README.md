# Visual Co-Creation Skill｜视觉共创 Skill

**开放式人机视觉共创 · Open-ended Human–AI Visual Co-Creation**

🌐 [简体中文](#简体中文) · [English](#english)

## 简体中文

### 项目简介

**Visual Co-Creation Skill 是一种开放式人机视觉共创工作流，而非固定风格的海报模板或提示词大全。**

它帮助 AI 从真实图片或文字想法中发现值得创作的视觉机会，通过简短对话共同完善创意，适时主动收束，将商定的视觉设计转化为专业、独立可执行的提示词。在用户**明确授权**之后才能实际生图或改图，并在评价作品时兼顾创意完成度与整体审美。

用户始终拥有最终的审美决定权。Skill 的目标是让 AI 成为**主动提出创意、能讨论也能判断的共创伙伴**，不是让所有作品都套入一种熟悉的风格。

> **当前版本：v0.3.0（实验版）**。尚未通过跨模型或 A/B 对照实测；**尚未选定复用许可证**。本仓库不包含生图模型，文本里的授权规则也不等于宿主平台已经部署了强制的工具调用拦截。

### v0.3 更新了什么？

本版强调**改进创作机制，而不是不断添加规则**：

1. **视觉机会发现（Visual Opportunity Search）**：分析素材的独特空间、材质、光线、结构与叙事关系，主动提出与画面相关的变化；将艺术媒介与风格视为可探索的创意方向。
2. **自适应创意对话**：默认每轮提出一个具体想法，认真吸收用户反馈，在创意与执行设计成熟时分别主动收束；不强迫用户反复选择 A/B，也不规定固定轮数。
3. **设计决策契约（Decision Contract）**：通过 `CORE / KEEP / CHANGE / AVOID / SOURCE / TEXT` 跟踪核心创意、保留项、修改项、否定项、底图身份与准确文字，避免修改时破坏已成功的内容。
4. **提示词编译器（Prompt Compiler）**：将充分的创意讨论压缩为高有效信息密度、可独立使用的执行提示词；删除重复、含糊修辞、无根据的微观要求，**不设置机械字数上限**。
5. **双轴作品评价**：分别判断**设计忠实度（Fidelity）**和**整体审美质量（Aesthetic Quality）**；局部更加符合要求，不代表整张作品一定更漂亮。
6. **授权与评测**：明确区分讨论、写提示词和生图，补充书面测试案例 E18–E25、运行记录模板和静态文档检查。

### 适合哪些请求？

| 你可以这样说 | Skill 将如何处理 |
| --- | --- |
| “这张照片能做成什么有意思的作品？” | 观察**实际上传的照片**，默认从画面本身提出一个具体且独特的创意。 |
| “我没有照片，想做一张关于末班车的原创海报。” | 从文字概念出发，不假装存在未上传的原图。 |
| “参考这张图的笔触，但不要复制里面的内容。” | 提取可迁移的视觉语言，区分原图、风格参考与构图参考。 |
| “想法不错，继续确定设计细节。” | 优先讨论真正重要的尺度、遮挡、材质、视觉重心和文字。 |
| “写提示词／优化提示词／自检提示词。” | **只交付文字，不调用生图工具。** |
| “这个生成结果为什么不对？” | 分开评价指令符合度、整体审美、已成功元素是否保留，并讨论改进方案。 |
| “现在正式生成／修改图片。” | 仅当**当前消息**明确授权、满足用户设定的触发条件、所需图片可用时才执行。 |

“ok”“继续”“试试”等模糊认可、上一轮的授权暗号、以及 AI 写在提示词中的暗号，都**不能单独授权生图**。可视化预览和自动重试同样受此约束。

如果用户已经提供完整设计，Skill 应直接完成请求，而不强制插入多轮创意讨论。

### 共创流程

**照片或想法 → 发现视觉机会 → 第一次收束（创意）→ 确定关键设计 → 第二次收束（执行）→ 编译完整提示词 → 用户授权后生图 → 评价／修改／停止**

这是灵活的协作节奏，**不是必须全部执行的六步脚本**。用户可以随时重新发散或换方向。

Skill 不预设某一种审美风格、极简留白比例、固定配色数量或默认使用超现实特效。必要时 AI 可以**提出**两个或三个具有真正不同视觉逻辑的预览方案，但不得未经授权直接生成。

### 项目文件

```text
SKILL.md                           核心行为、请求路由、生图授权
references/
  visual-analysis.md               图像角色、可观察特征、参考图分析
  creative-discovery.md            创意机会发现与风格探索
  prompt-engineering.md            决策转化为高信息密度提示词
  iteration-and-evaluation.md      双轴评价、修改与止损
examples/
  two-entry-routes.md              虚构的共创对话示例
evaluations/
  evaluation-cases.md              25 个书面行为测试案例
  run-log-template.md              测试及工具调用记录模板
scripts/
  lint_skill.py                    静态文档完整性检查
.github/workflows/skill-lint.yml   GitHub Actions 静态检查
README.md
CHANGELOG.md
```

Agent 从 [SKILL.md](SKILL.md) 开始，仅在需要时加载相应参考文件。这是一种**渐进式加载（Progressive Disclosure）**：核心规则始终简洁，专项知识按任务读取。

### 安装与使用

将仓库加载到兼容 [Agent Skills 规范](https://agentskills.io/specification) 的宿主环境中。安装、自动触发和版本更新方式依具体平台而异；实际绘图需要额外的图像生成／编辑工具。

在普通聊天中也可以直接读取 `SKILL.md` 与相关参考文件，按照其中规则合作；但**读取文档不等于在平台中安装 Skill**。

示例指令：

- “这里有张街头照片，我们先一轮一个点子地探索。”
- “我没有参考图，帮我构思关于初雪的原创画面。”
- “对比这些海报，提炼固定与可变化的视觉规则。”
- “设计已经定下来了，写完整精炼的提示词，但不要生图。”
- “两次生成各有什么优缺点？哪张更符合目标，哪张更好看？”

### 测试和证据

仓库包含 **25 个书面行为测试场景**及[运行记录模板](evaluations/run-log-template.md)。目前**没有**足以证明 v0.3 比 v0.2 或不启用 Skill 更有效的对照测试结果。

运行静态检查：

```bash
python3 scripts/lint_skill.py .
```

它能够检查文件完整性、版本一致性、Markdown 相对链接和评测编号；**不能**验证 AI 是否正确调用工具、是否遵守生图授权，或成品审美是否提升。这些需要真实的工具调用日志、用户反馈和对照实验。详见[评测案例](evaluations/evaluation-cases.md)。

**隐私：** 仓库示例均为虚构，不会未经许可公开用户照片或私人创作记录。

### 研究参考

本项目参考并选择性吸收了 [frontend-slides](https://github.com/zarazhangrui/frontend-slides)、[gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)、[ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)、[ui-skills](https://github.com/ibelick/ui-skills)、[guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) 和 [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) 的方法论，但不直接复制其代码或固定风格模板。

### 许可证

**目前尚未选择许可证。** GitHub 仓库公开可见，不意味着自动允许复制、修改或再分发。

---

## English

**An open-ended human–AI visual co-creation process—not a fixed style pack or a prompt-length contest.**


> **Status: v0.3.0 — Experimental / not behavior-benchmarked.** Public repository, **no reuse license selected yet**. The Skill does not include an image model, and its written permission rules are **not a host-level tool interceptor**.

## What changed in v0.3

The priority is **mechanism, not more rules**:

1. **Visual Opportunity Search**: observe what is distinctive in this image, propose an actual transformation, then treat visual style/medium as an experimental hypothesis.
2. **Adaptive creative dialogue**: one genuinely concrete seed per turn by default, user feedback changes the idea; proactively announce **concept** and **execution** convergence when ready.
3. **Decision Contract**: `CORE / KEEP / CHANGE / AVOID / SOURCE / TEXT` prevents discarded ideas from returning and protects already successful regions.
4. **Prompt Compiler**: compile agreed visual constraints into a standalone, high-information-density prompt. Remove repetition, invented micro-decisions and narrative justification; **no fixed word count**.
5. **Fidelity × Aesthetic Quality**: a more compliant image is not always a better image. Protect existing aesthetic strengths and stop fruitless iteration.
6. **Consent & testing**: route prompt-only requests separately from execution; respect the **current user's** explicit image-tool permission and any personalized trigger. Add written behavioral cases E18–E25, a test-log template and static documentation lint.

## Requests and entry routes

| What the user asks | Skill behavior |
| --- | --- |
| “Here is a photo, any interesting ideas?” | Analyze the **actual photo** and explore one source-specific creative move. |
| “No photo, imagine a scene about …” | Explore from the text, without inventing a reference image. |
| “Use this reference only for its brushwork” | Extract transferable grammar; do not copy source text or composition. |
| “I like the idea; help settle the details” | Resolve only important design choices; converge proactively. |
| “Write / improve / self-check the prompt” | Return **text only**, no image-tool call. |
| “What's wrong with this output?” | Separate design fidelity, aesthetic quality, preservation and feasible next moves. |
| “Generate/edit now” | Execute **only** if the current request meets the user's authorization conditions and the needed source is available. |

A pasted assistant-authored trigger, an old message, or a reply such as “ok,” “continue,” or “try it” is not permission. Users can establish stricter trigger phrases. No preview or retry is generated without authorization.

For a fully specified task, the Skill should **skip unnecessary dialogue**. The two convergence points are helpful checkpoints during exploration, not a mandatory sequence.

## Workflow

**Image or idea → concrete creative opportunity → first convergence → key design decisions → second convergence → standalone prompt → expressly authorized generation → fidelity/aesthetic review (or stop).**

Creative ideation remains open to any medium, style, density or visual mechanism. The Skill does **not** enforce an aesthetic whitelist, a fixed 3-color palette, a mandatory number of previews, a maximum prompt length, or auto-generated "variants."

If comparative visual previews could help, the agent may **suggest** 2–3 distinct options, but must not invoke image tools before authorization.

## Repository structure

```text
SKILL.md                           core behavior, mode routing, authorization
references/
  visual-analysis.md               image roles, factual observation, reference grammar
  creative-discovery.md            visual opportunity and style exploration
  prompt-engineering.md            decision-to-pixels compiler and preflight
  iteration-and-evaluation.md      two-axis critique, side effects and stop rules
examples/
  two-entry-routes.md              fictional co-creation scenarios
evaluations/
  evaluation-cases.md              25 written manual behavior tests
  run-log-template.md              reproducible tool/aesthetic audit template
scripts/
  lint_skill.py                    static repo integrity check (NOT behavior proof)
.github/workflows/skill-lint.yml   CI runs the static check
README.md
CHANGELOG.md
```

The agent starts with [SKILL.md](SKILL.md) and consults each [reference](references/visual-analysis.md) only when relevant. This is **progressive disclosure** of specialized instructions, not an invitation to load every file into each turn.

## Installation and use

Load/install the repository in a host supporting the [Agent Skills format](https://agentskills.io/specification). The host decides the exact installation and activation interface. An independent image editing/generation tool is needed for renders; the Skill itself does not ship an image model or guarantee editing fidelity.

Example requests:

- “Here is a street photo. Explore one unexpected visual idea at a time.”
- “I have no source image; let's invent a graphic scene about first snow.”
- “Compare these references and extract their fixed, variable and sample-specific style rules.”
- “Our concept is settled. Write a concise complete prompt; **do not generate**.”
- “Compare these two results: what improved fidelity, and what lost visual appeal?”

## Validation and evidence

The repository has **25 written manual evaluation cases** and a [run-log template](evaluations/run-log-template.md). No claim is made that an agent passed them; **v0.3 has not been A/B benchmarked** against v0.2 or no-Skill baselines.

Run the static integrity check locally:

```bash
python3 scripts/lint_skill.py .
```

It checks expected files, frontmatter/version alignment, relative Markdown links and case IDs. It cannot check image-tool calls, user preference, rendered aesthetics or generative model behavior. These require host tool logs and real trials, with human review as described in [evaluations/evaluation-cases.md](evaluations/evaluation-cases.md).

**Privacy:** examples are invented; user photos and creative conversations must not be copied into public tests without consent.

## Research influences

The design selectively studies public Skills such as [frontend-slides](https://github.com/zarazhangrui/frontend-slides), [gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster), [ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill), [ui-skills](https://github.com/ibelick/ui-skills), [guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) and [gzh-design-skill](https://github.com/isjiamu/gzh-design-skill). Ideas were adapted to this broader, style-agnostic workflow; no third-party implementation or theme pack was copied.

## Licensing

**No license chosen.** A public GitHub repository does not, by itself, give permission to copy, modify, or redistribute its contents.
