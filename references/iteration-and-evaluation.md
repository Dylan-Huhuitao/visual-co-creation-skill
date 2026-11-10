# Critique, Diagnosis & Iteration

Use after the user shows a result or asks to evaluate a generated image. The benchmark is the **agreed visual intent**, not the agent's taste or average attractiveness.

## Evaluate in layers

1. **Core idea:** Is the chosen visual mechanism present, or did the output merely imitate its subject matter?
2. **Brief fidelity:** Are required and protected elements preserved? Is exact text correct?
3. **Composition:** Are scale, focal hierarchy, spacing, cropping, depth, foreground/background relations working?
4. **Physical logic:** Are shadows, reflections, light sources, perspective and occlusion plausible if relevant?
5. **Material and atmosphere:** Do style, surfaces, texture, color, type, and lighting serve the selected idea?
6. **Experience:** Does the result communicate its intended impact? This is a reasoned interpretation, not a universal rating.

Report a small number of decisive observations, grounded in the visible result. Do not invent visual details you cannot inspect.

## Diagnose before changing

Possible defect categories:

| Type | Example | Response |
| --- | --- | --- |
| Concept | The visual metaphor itself is weak | Reconsider the mechanism with the user |
| Decision | Selected direction lacks spatial specificity | Resolve composition/causality |
| Prompt | Clear plan is incompletely communicated | Rewrite concise actionable instruction |
| Stochastic | Model missed one instruction once | Retry or targeted edit if justified |
| Capability | Repeated failures on coherent complex geometry | Change strategy: diagram, masks, layers, 3D or manual composition |
| Preservation | A successful object vanished during a local edit | Explicitly lock protected regions/elements |

Distinguish diagnosis from certainty. Without controlled tests, “capability limit” is often a plausible explanation, not a proven root cause.

## Select edit scale

**Local:** only a small detail is wrong. Specify exactly what changes and protect the rest.

**Structural:** the central concept is good but layout, light, scale, perspective, or interaction is wrong. Revise those relationships while keeping the concept.

**Conceptual:** the chosen premise is no longer suitable. Explicitly reopen exploration with the user's agreement; do not silently abandon it.

## Revision protocol

First identify:

- **Keep:** already successful features.
- **Fix:** the 1–3 most consequential mismatches.
- **Why:** likely design, prompting or technical cause.
- **Do not change:** essential scene and image identity, plus any non-negotiables.

Then produce a new self-contained prompt when the user asks for it. Never make an unrequested image edit in the course of critique. After the revised result is provided, repeat evaluation; check whether previous successes survived.

Avoid endless optimization of low-impact details. Stop when the user is satisfied or when further work cannot reliably help.

## Memory and evidence

Record transferable principles, not private conversations by default. Do not silently export user images or private chat content into public documentation.

For project improvement, log the original goal, selected concept, iterations, failure hypotheses, and outcomes (with user consent where needed). Distinguish verified behavior from anecdotal impressions.

## How to evaluate the skill itself

Test the **agent with the skill versus the same agent without it**, using comparable prompts, tools and time budgets. For images, assess repeated runs because outputs are stochastic. Measure satisfaction, intent fidelity, novelty, revisions required and unwanted changes. Early feedback is exploratory evidence, not proof of general superiority.
