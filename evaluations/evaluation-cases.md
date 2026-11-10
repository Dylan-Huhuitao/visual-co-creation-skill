# Behavioral Evaluation Cases — v0.1.0

**Status:** written test specifications only; **not** an executable test suite or completed benchmark. These cases should be run manually with an agent that has the skill enabled, and ideally repeated with the same agent/model/tools without the skill.

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

**Pass:** Agent observes identifiable features, finds opportunities grounded in the image, offers genuinely different concepts and asks for selection before writing a definitive prompt.

**Fail:** Generic style menu, hallucinates unobserved features, or immediately generates.

### E02 — Route A with an initial editing idea

**Input:** Photo plus “I want to explore the shadows as part of the story.”

**Pass:** Agent develops the user's shadow idea, preserves photo identity, proposes concrete shadow–subject relationships and trade-offs; does not replace the idea with an unrelated poster trend.

**Fail:** Ignores user's idea, invents unsupported geometry.

### E03 — Route B without a source image

**Input:** “Make an original scene about a quiet train station after the last departure. I have no photo.”

**Pass:** Builds from text, offers differentiated spatial/narrative concepts; final prompt (after selection) works without photo attachments.

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

## Scoring and report template

Score 0–2 for each applicable category: **intent alignment**, **source-aware or text-aware analysis**, **creative differentiation**, **decision coherence**, **prompt specificity**, **feedback quality**, **authorization/preservation discipline**. Mark N/A where a category does not apply; report numerator and available denominator, not a falsely uniform total.

For every run, record:

- Date, platform, model/tool configuration, skill version, case ID and input.
- Whether an image was available and which entry route was used.
- Observed output and any generated-image artifacts.
- Each score with brief evidence.
- Critical failures and proposed skill revisions.

### Release interpretation

A file full of cases is *not* evidence that they pass. v0.1.0 is an experiment. Revisit the instructions only after understanding whether a failure is generalizable, task-specific, or due to model variance.
