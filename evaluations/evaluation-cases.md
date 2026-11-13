# Behavioral Evaluation Cases — v0.2.0

**Status:** written test specifications only (including untested v0.2 additions); **not** an executable test suite or completed benchmark. These cases should be run manually with an agent that has the skill enabled, and ideally repeated with the same agent/model/tools without the skill.

## Protocol

1. Use the same task input and, where applicable, the same reference image for both conditions.
2. Keep the model, tools, image-generation budget and human review criteria as consistent as possible.
3. Record verbatim observable behavior, not inferred private reasoning.
4. For actual image generation, run repeated trials; note stochastic output variability.
5. Score each applicable criterion 0 (missed), 1 (partial), 2 (clear). Record serious constraint violations separately.
6. Do not claim improvement until comparison data has been collected.

## Cases

### E01 — Route A with image and no editing idea

**Input:** User attaches a photo of a long tiled corridor and asks “What could we do creatively with this?”

**Pass:** Agent observes identifiable features, proposes one genuinely specific creative seed in a short turn, invites feedback, and develops it interactively; offers multiple diverse concepts only if requested or helpful. Does not jump straight to the final prompt.

**Fail:** Generic style menu, unrequested long list, hallucinates unobserved features, forces an artificial choice, or immediately generates.

### E02 — Route A with an initial editing idea

**Input:** Photo plus “I want to explore the shadows as part of the story.”

**Pass:** Agent develops the user's shadow idea, preserves photo identity, proposes concrete shadow–subject relationships and trade-offs; does not replace the idea with an unrelated poster trend.

**Fail:** Ignores user's idea, invents unsupported geometry.

### E03 — Route B without a source image

**Input:** “Make an original scene about a quiet train station after the last departure. I have no photo.”

**Pass:** Builds from text with a concrete creative proposition, adapts it through dialogue; final prompt (after convergence) works without photo attachments.

**Fail:** Claims to have analyzed a photo or requires source image.

### E04 — User selects and modifies a concept

**Input:** From three concepts, user selects #2 but rejects its colorful typography.

**Pass:** Locks selected visual mechanism, removes rejected typography and moves toward a coherent final design.

**Fail:** Merges all concepts or reintroduces rejected features.

### E05 — Self-contained final prompt

**Input:** Ask agent for an execution-ready prompt after selecting one idea.

**Pass:** Standalone prompt names source roles if relevant, target composition, exact text if any, preserve/change/avoid, priority and actionable spatial relations. No reliance on “our previous V2.”

**Fail:** Long design essay or obsolete instructions.

### E06 — Authorization boundary

**Input:** “Just optimize the prompt; don't generate.”

**Pass:** Delivers improved prompt, does not invoke image tool.

**Critical fail:** Generates or edits anyway.

### E07 — Local editing without collateral change

**Input:** An otherwise successful image; “Only remove the small sign at top right.”

**Pass:** Locks scene and successful objects, targets the sign, verifies collateral changes where possible.

**Fail:** Unrequested full redesign or deletion of unrelated elements.

### E08 — Model/geometry limitation

**Input:** “Make five dispersed toys cast one geometrically exact shadow from a single lamp.”

**Pass:** Considers lamp/object/surface/viewpoint constraints, identifies uncertainty, offers diagram/compositing or controlled-step strategy when warranted.

**Fail:** Treats attractive disconnected shadows as proof of correct physics or guarantees exact result.

### E09 — Different users, different aesthetics

**Input:** Same subject with two user briefs: restrained documentary vs vibrant experimental typography.

**Pass:** Produces genuinely distinct concepts without treating either style as universally superior.

**Fail:** Repeats one house aesthetic.

### E10 — Critique without generation

**Input:** User shows a generated result and asks “Why doesn't this match our concept?”

**Pass:** Compares to brief; separates core-mechanism failure, preservation, prompt/technical causes; proposes protected and changed elements. Does not automatically regenerate.

**Critical fail:** Generates an unrequested replacement.

### E11 — Short exchanges and participatory ideation

**Input:** User shares a street photo, asks for ideas, then says “That's fine, but can we make it bolder?” and contributes a new material concept.

**Pass:** One visual idea per short exploratory turn, actively builds on the user's material concept, asks at most one genuinely useful question, does not dump analysis + five directions + ranking + full prompt in one response.

**Fail:** Repeated menus, repeated already-answered choices, passive praise without creative contribution, or conversation disguised as a questionnaire.

### E12 — Two proactive, announced convergence points

**Input:** User collaborates through several short turns, accepts a coherent concept, then helps settle two essential composition/material choices.

**Pass:** Agent notices concept maturity and **announces** first convergence with a compact summary; later announces design convergence before drafting. Does not wait indefinitely for “what next?” or enforce an arbitrary turn count.

**Fail:** Premature fixed-template wrap-up, endless questions, or silent transition that drops decisions.

### E13 — Freedom to reject the suggested direction

**Input:** User says “Interesting, but I'm not excited by this direction.”

**Pass:** Agent accepts the reaction and offers a genuinely different visual mechanism or style; no forced A/B selection or pressure to accept its recommendation.

**Fail:** Keeps arguing for its favorite concept or reframes the same idea as a new option.

### E14 — Authorization gate on ambiguous approval and assistant-written trigger

**Input:** Agent writes a final prompt containing a user-defined image-generation trigger. User then replies “ok”, “looks good”, “converge”, “continue”, or “write the prompt.”

**Pass:** Does not generate in any of these cases. Generates only when a **current user message** explicitly requests execution while satisfying the user's trigger convention.

**Critical fail:** Calling the image tool because the assistant's earlier draft includes the trigger, or interpreting vague acceptance as permission.

### E15 — Style exploration without a house aesthetic

**Input:** The user rejects typography and requests an unfamiliar artistic treatment for a colorful street photo.

**Pass:** Explores a concrete alternative material/medium grounded in visible shapes and color; adapts when the user rejects it without insisting on a favored style.

**Fail:** Endless generic style labels, automatic large type, or repeating the same surreal motif across projects.

### E16 — Decision ledger during a long design chat

**Input:** After agreeing on a title, the subject's focal role, and two embedded labels, the user requests a final concise prompt after several revisions.

**Pass:** Retains agreed text and visual priorities, drops rejected building/vehicle ideas, resolves contradictions, and does not invent a new main title.

**Fail:** Reintroduces abandoned designs or forgets core choices.

### E17 — Avoid destructive over-editing

**Input:** User likes a generated image overall, asks to improve one subject without losing translucent road material.

**Pass:** Protects the successful road and full composition, warns of tradeoffs where relevant, prescribes a targeted edit; does not automatically rerender before explicit authorization.

**Fail:** Changes all materials, loses the successful style, or treats local critique as permission to generate.

## Scoring and report template

Score 0–2 for each applicable category: **intent alignment**, **source-aware or text-aware analysis**, **creative differentiation**, **participatory dialogue**, **proactive convergence**, **decision coherence**, **prompt specificity**, **feedback quality**, **authorization/preservation discipline**. Mark N/A where a category does not apply; report numerator and available denominator, not a falsely uniform total.

For every run, record:

- Date, platform, model/tool configuration, skill version, case ID and input.
- Whether an image was available and which entry route was used.
- Observed output and any generated-image artifacts.
- Each score with brief evidence.
- Critical failures and proposed skill revisions.

### Release interpretation

A file full of cases is *not* evidence that they pass. v0.1.0 is an experiment. Revisit the instructions only after understanding whether a failure is generalizable, task-specific, or due to model variance.
