# Visual Co-Creation Skill

**Help AI draw on its broad visual knowledge to co-create images with people—without locking anyone into a preset aesthetic.**

**中文简介：** 一个以用户审美判断为核心的 Agent Skill。它帮助 AI 主动发现视觉可能性，将用户选择转化成清晰可执行的生图／改图提示词，并通过反馈逐步修正作品。它不是某一种风格模板，也不是提示词大全。

> **Status:** v0.1.0 — Experimental. This project is public for inspection; a reuse license has not been selected.

## Why

A model may know many approaches to composition, visual narrative, typography, texture, lighting and design. A difficult step is **selecting the right approach for this image, this idea and this person**, then executing and evaluating it faithfully.

This skill experiments with a collaborative process for that selection. The user remains the creative authority; the agent supplies analysis, imaginative alternatives, decision support, actionable prompts and candid critique.

## Two ways to start

**A. Image-led redesign / 图片二创：**

1. You provide a photograph or image, optionally with an editing idea.
2. The agent studies its distinctive structures and offers creative directions.
3. You choose or revise a direction until the concept is settled.
4. The agent writes a complete editing prompt; you review/copy it and submit it with the source image when you want to generate.
5. You inspect the result and continue targeted revisions until satisfied.

**B. Idea-led creation / 文字原创：**

1. You provide an initial text-to-image idea; no source photo is necessary.
2. The agent develops and diversifies the concept.
3. You select or revise a direction.
4. The agent writes a complete text-to-image prompt; you explicitly submit it for generation.
5. You evaluate and refine the result.

Both routes share the same key checkpoints: **creative exploration → user choice → finalized visual decisions → prompt → explicit generation → critique → iteration**.

The workflow adapts to the task: a fully specified request should not be slowed down by unnecessary proposals.

## Principles

- **Style-agnostic:** no permanent “best” style, density, palette or composition.
- **Creative contribution:** propose distinct visual *mechanisms*, not just superficial variants.
- **User-led:** the user decides what is worth making.
- **Decision-first prompting:** final prompts contain current actionable visual decisions, not discarded brainstorming.
- **Preservation-aware editing:** distinguish what to keep, change, and avoid.
- **Permission-aware:** drafting a prompt alone never triggers image generation.
- **Honest limits:** model failures may require tools or strategies beyond longer prompts.

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

- “Here is a street photograph. Find three genuinely different design directions.”
- “我没有参考图，想做一张关于初雪的海报，先帮我探索创意。”
- “I chose the spatial-typography concept. Write the final prompt, but don't generate yet.”
- “Compare this output with the agreed concept; preserve the parts that work.”

For a self-contained image prompt, explicitly provide any required source/reference images when you submit it for execution. If your agent supports direct image generation, the agent should respect your explicit authorization rules.

## Scope and evidence

The initial methodology draws mainly on a limited set of image-led, photography/editorial-design collaborations and iterative prompting experience. **Text-first creation, reliable multi-object physical simulation, generalization across users, and across-model performance are not yet established.** v0.1.0 is a usable specification for experimentation, not a validated claim of higher image quality or stable success rates.

See [evaluations/evaluation-cases.md](evaluations/evaluation-cases.md) for reproducible behavioral scenarios. We welcome concrete observations, failures and improvements, without needing to publish private creative chat logs or original photographs.

## Licensing

**No license has been chosen yet.** Public visibility does not by itself grant permission to copy, modify or redistribute this repository. A license can be added when its terms have been reviewed and agreed.
