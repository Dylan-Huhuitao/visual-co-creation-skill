# Visual Co-Creation Skill

**Help AI draw on its broad visual knowledge to co-create images with people—without locking anyone into a preset aesthetic.**

**中文简介：** 一个以用户审美判断为核心的 Agent Skill。它帮助 AI 主动发现视觉可能性，将用户选择转化成清晰可执行的生图／改图提示词，并通过反馈逐步修正作品。它不是某一种风格模板，也不是提示词大全。

> **Status:** v0.2.0 — Experimental. This project is public for inspection; a reuse license has not been selected.

## Why

A model may know many approaches to composition, visual narrative, typography, texture, lighting and design. A difficult step is **selecting the right approach for this image, this idea and this person**, then executing and evaluating it faithfully.

This skill experiments with a **short-turn, co-discovery dialogue**. The agent contributes one concrete visual move at a time, invites the user's changes, and **proactively announces convergence** when the concept and later the execution design are sufficiently mature. The user remains the creative authority; the agent supplies creative contributions, judgments, actionable prompts and candid critique.

## Two ways to start

**A. Image-led redesign / 图片二创：** Start from an actual image. The agent inspects its distinctive structure and revisits it when new spatial decisions require verification.

**B. Idea-led creation / 文字原创：** Start from a textual idea, with no invented or required photograph.

Both follow a flexible rhythm:

**Brief creative dialogue → first proactive concept convergence → a few decisive design details → second proactive design convergence → concise complete prompt → explicitly authorized generation → critique/refinement.**

Not every task needs every stage. The agent can reopen exploration if a new idea improves the work, and skips discovery when the user already has a complete brief.

## Principles

- **Co-create, don't quiz:** Default to one imaginative, concrete visual idea per short message; invite correction, synthesis or a wholly different direction.
- **Source-aware, style-agnostic:** Use the image's actual composition and broad visual/artistic knowledge; do not impose giant typography, surrealism or any other default.
- **Proactive but not controlling:** Announce when the concept/design is ripe for convergence; the user can reopen or refuse it.
- **Adaptive tone:** Humor, warmth and emoji only when the user welcomes them; remain concise and substantive.
- **Decision memory:** Preserve agreed/working/rejected choices across turns; protect successful visual features during revisions.
- **Professional prompts:** Give precise, stand-alone, non-repetitive execution instructions, without overconstraining minor details.
- **Strict consent:** Prompt writing, “ok,” “continue,” or a trigger phrase written **by the agent** never independently authorizes rendering. The user's current explicit generation request and any special trigger are required.
- **Candid limits:** Complex physical logic or repeated failures may call for simpler methods, targeted edits, or abandoning an idea rather than more prompt verbosity.

## Repository structure

```text
visual-co-creation-skill/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── references/
│   ├── visual-analysis.md
│   ├── prompt-engineering.md
│   └── iteration-and-evaluation.md
├── examples/
│   └── two-entry-routes.md
└── evaluations/
    └── evaluation-cases.md
```

**SKILL.md** is the operational instruction file. **references/** contains methods read only as needed. **examples/** demonstrates both entry routes using synthetic cases, not private conversations. **evaluations/** contains manual behavioral tests, **not executable code**.

## Use it

Install or load this repository as a skill in a host agent that supports the [Agent Skills format](https://agentskills.io/specification). Installation commands and automatic activation depend on the host. Image generation or editing requires a separate supported image tool; this skill does not ship or train an image model.

Try prompts such as:

- “Here is a street photograph. Let's explore one interesting visual idea at a time.”
- “我没有参考图，想做一张关于初雪的海报，先帮我探索创意。”
- “I chose the spatial-typography concept. Write the final prompt, but don't generate yet.”
- “Compare this output with the agreed concept; preserve the parts that work.”

For a self-contained image prompt, explicitly provide any required source/reference images when you submit it for execution. If your agent supports direct image generation, the agent should respect your explicit authorization rules.

## Scope and evidence

V0.2 incorporates qualitative observations from a small number of image-led collaborations, including a successful short-turn exploration, a failed over-complex spatial design, and a material-style exploration with regressive edits. These are **design hypotheses, not benchmark results**. Text-first creation, generalization across users/models, and generation authorization compliance still require real-world tests. This specification does not claim measured superiority.

See [evaluations/evaluation-cases.md](evaluations/evaluation-cases.md) for 17 manual behavioral scenarios (written only; none are passed automatically). We welcome concrete observations, failures and improvements, without needing to publish private creative chat logs or original photographs.

## Licensing

**No license has been chosen yet.** Public visibility does not by itself grant permission to copy, modify or redistribute this repository. A license can be added when its terms have been reviewed and agreed.
