# Prompt Compiler — Decision to Pixels

Load when drafting, optimizing or self-checking a **final image prompt**. A final prompt is a compact **execution specification**, not a transcript of how the idea emerged. It must make sense in a fresh conversation with the stated attached source(s).

## Step 1 — Freeze the decision contract

Assemble the current user's decisions before writing:

```text
CORE    one indispensable visual relationship or goal
KEEP    up to three important source invariants or previously successful features
CHANGE  up to three intended transformations
AVOID   rejected decisions and demonstrated failure modes (only relevant ones)
SOURCE  original photo reconstruction / selected generated edit / style-only reference / insert / text-only
TEXT    exact requested spelling, capitalization, priority and placement (if any)
```

This is an **internal ledger**, not a form the user must fill out. Use the latest decisions, not old drafts. A newer instruction can reopen an earlier keep/avoid item.

## Step 2 — Choose source contract

**Fresh image from an original photo:** explicitly name the supplied original as the base, what identity and composition remain recognizable, and what can be reinterpreted.

**Local edit of a selected generated result:** name **that** result as the edit base, specify only the changed region/objects, and lock the selected successful styling/composition. Do not accidentally use the original.

**Reference-only style:** identify which image is a style/composition/technical reference; specify transferable visual grammar, not incidental source subjects, words or signatures.

**Text-first creation:** specify subjects, material, visual relations and framing; do not invent a reference image.

## Step 3 — Compile in descending importance

Include only fields relevant to the brief, roughly in this order:

1. **Input, intended output, and keep/change boundary.**
2. **Core visual event:** the primary imageable relationship and focal hierarchy.
3. **Essential execution geometry:** location, scale, perspective, occlusion, interaction and material/lighting behavior that determine whether the concept works.
4. **Exact user text:** wording, capitalization, placement, visual weight when specified.
5. **Few relevant avoids:** demonstrated failure risks and destructive side effects.

Use language a renderer can translate into visible pixels. Describe **what it should look like and how objects relate**, not why the concept is profound or what viewers should feel at first glance. Define the materials and style at the level that changes visible results, without dictating every highlight, leaf or stripe.

## Step 4 — Information-density deletion pass

Before delivery, delete or merge:

- Prior discussion, motivation, praise, abandoned alternatives and superseded versions.
- Repeated “highest priority,” redundant clauses and generic forbidden-style catalogs.
- Invented numeric precision and details the user did not choose.
- Instructions unlikely to change observable output, or likely to compete with the focal mechanism.
- Ambiguous sensory adjectives not tied to material, lighting, color, composition or stroke behavior.

Ask for each sentence: **“If I delete this, do I lose a meaningful visible requirement?”** Keep an instruction only if it materially changes the target image, protects user intent, or prevents a known serious failure. No mandatory paragraph count or word limit; complex tasks can legitimately need more.

**Complexity budget is goal-dependent**, not fixed. Silhouette legibility may need simple shapes; an experimental maximalist poster may require density. Do not import generic requirements like three colors, 70% whitespace or one font.

## Important failure mode: two visual media in one small object

“Half oil painting, half real” can be misread as **two colors**, a smooth 3D material, or a decorative overlay. When essential, describe the **contrasting physical surfaces**: visibly piled pigments, raised directional brush ridges and irregular painted edges **versus** thin translucent biological petals and photographic microtexture, on the same connected flower. Keep hue consistent if color splitting is not intended.

This does **not** guarantee the generator can perform precise local material segmentation. After repeated misses, diagnose capability or method, not automatically a missing paragraph of instructions.

## Optional compact prompt shapes (not mandatory templates)

**Original-photo reconstruction:** “Use the attached original [subject/photo] as the edit target. Preserve [3 concrete invariants]. Reinterpret [region/content] as [one precise visual mechanism and chosen style/material]. Place [focal relationship, key occlusion]. Keep [exact text]. Avoid [few known failures].”

**Selected-result local edit:** “Edit the attached [selected result], not the original source. Preserve [already successful regions/style/text]. Change only [local elements] to [visible target relationship]. Maintain [crucial contacts/occlusions]. Leave [protected details] unchanged.”

**Text-first:** “[Subject] in [setting/medium], arranged as [central geometry and action]; [material/light/hierarchy]. Include [exact text if any]. Avoid [only critical exclusions].”

All are adaptable; a truly simple task may require only two sentences.

## Final preflight

- Correct source image role? Actual source attached/identified?
- Does every indispensable CORE/KEEP/TEXT constraint survive the compression?
- Are spatial and material relations internally coherent and observable?
- Have rejected directions and unrequested extra details been excluded?
- Is the final prompt independently executable without old chat references?
- Is this **prompt-only** or a genuinely **authorized execution** request? An assistant-written trigger inside this prompt is **not** permission to call an image tool.

Deliver the copyable prompt only when asked. Even an otherwise perfect prompt never overrides the image-tool authorization gate.
