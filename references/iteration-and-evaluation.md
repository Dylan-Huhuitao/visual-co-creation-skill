# Two-Axis Critique, Revision and Stopping

Load when a user asks about a generated result, a proposed revision, or repeated failures. Actually inspect the available image(s). The benchmark is the user's agreed design, not the model's favorite style.

## Evaluate three separate questions

**1. Fidelity — Did it do the thing?**

Check the essential visual event, source identity, exact text, geometry, occlusion, and material contrast. Do not grant fidelity merely because the theme or color looks vaguely similar.

**2. Aesthetic quality — Is the whole image compelling?**

Judge spatial hierarchy, stylistic integration, color rhythm, visual surprise and compositional coherence. These are **reasoned, contextual evaluations**, not mechanically objective scores. A locally “fixed” bus, title or flower can lower total quality.

**3. Preservation — Did previous strengths survive?**

Check the user's protected KEEP elements: previously successful materials, contrast, framing, lettering or emotional temperature. A local request is not permission for unrelated redesign.

Make the dual-axis trade-off explicit when it matters: “more compliant, less cohesive” is a meaningful diagnosis.

## Diagnose the likely failure mode

| Likely source | Observable symptom | Proportionate response |
| --- | --- | --- |
| **Concept** | Device is arbitrary or aesthetically unconvincing even if executed | Reopen ideation if user wants. |
| **Design** | Contradictory geometry, clutter or poor focal relationships | Simplify relationships or resolve one key dependency. |
| **Prompt** | Model never received a concrete essential instruction | Rewrite that relation clearly; do not expand everything. |
| **Stochastic** | A single run misses an otherwise clear constraint | Consider independent reroll **only if authorized**. |
| **Capability/method** | Same localized geometry or material mix repeatedly fails | Suggest masking, manual compositing, different medium or accepting the best image. |
| **Source preservation** | A winning region or text is lost during a small fix | Correct the source role and tighten protected region. |

A repeated failure is evidence for a **hypothesis**, not proof that a model is intrinsically incapable. Distinguish a problem in the aesthetic plan from an execution problem.

## Choose the minimum helpful next move

- **Local:** one feature fails; preserve everything else. Warn if the editing method cannot reliably preserve it.
- **Structural:** retain concept, change framing/occlusion/material hierarchy.
- **Conceptual:** user no longer believes in the idea; offer another genuinely different mechanism.
- **Preserve/stop:** current version is already attractive and another edit has poor expected value.

When asked to revise a prompt, produce a **self-contained** one with the correct chosen base image. When only asked to discuss a result, discuss it; **do not invoke image generation**.

## Repetition and stopping

After **2–3 materially similar misses** despite a clear requirement, stop treating longer prompts as the default fix. Propose a meaningful strategy change, independent sample (with authorization), simpler concept, selective compositing, preservation of the best result, or ending the project. Do not forcibly cut off exploration if the user wants to continue; offer an informed stop rule and make its rationale clear.

Judge a new result against the **best prior version**, not just the most recent one. A small gain in fidelity does not automatically justify loss of aesthetic unity.

## Evidence vs narrative

- Report directly visible facts separately from aesthetic interpretation.
- Make remaining failures explicit without lengthy disclaimers.
- Track repeatable failure patterns privately with permission; do not publish personal photos/conversations in the Skill repository.
- For Skill effectiveness, compare enabled vs disabled or V0.2 vs V0.3 under comparable model, prompts and generation budgets; repeated image trials and human preference judgments are necessary to support a measured improvement claim.
