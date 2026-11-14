# Visual Co-Creation Skill

**An open-ended human–AI visual co-creation process—not a fixed style pack or a prompt-length contest.**

**中文：** 帮助 AI 观察真实图片、主动发现创意、与用户短轮次讨论、适时主动收束、将设计编译为有效提示词，并在用户授权后执行图像生成与作品评价。用户对美学方向拥有最终决定权。

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
