# Decision-First Prompt Construction

A final image prompt is an **execution specification**, not a narrative of how the concept was discovered. It must be usable in a fresh context with the required image attachments and must not depend on remembered previous drafts.

## Step 1 — Freeze the current concept

Before drafting, collect:

- Chosen premise and central visual mechanism.
- Intended format and composition.
- P0/P1/P2 constraints.
- Exact source/reference roles.
- Text to render, if any, including wording, capitalization and placement.
- Essential keep/change/avoid boundaries.
- Known execution risks.
- Lightweight decision ledger: agreed, tentative, rejected, already successful. Exclude rejected and superseded choices, even if they appeared in a previous prompt.

Exclude discarded variants and obsolete feedback. If the user has not made a selection, do not pretend that a chosen concept exists.

## Step 2 — Choose prompt type

### A. Editing an existing image

Identify the **specific attached image as the edit base**. Distinguish:

- **Keep:** identity-critical structures, object count/positions, typography, camera perspective or other protected features.
- **Change:** exact subject/region/relationships to alter.
- **Add:** new elements and how they physically/spatially connect.
- **Avoid:** likely unwanted changes that would violate the brief.

Do not refer to “V2” or “the good parts we discussed” unless a particular supplied image is explicitly identified as that version. A new generation from a source photo is not equivalent to a targeted edit of an already successful generated result.

### B. Creating an image from a text idea

State subject, environment, action or visual metaphor, composition, hierarchy, lighting, materials, medium, text and constraints as needed. **Do not require a photo that does not exist.**

## Step 3 — Describe relationships rather than adjectives

Prefer observable arrangements: where, how large, which layer, which object occludes another, where the eye moves, how text meets architecture, which region receives light, and which surface carries a shadow.

Example:

Weak: “Make it editorial, sophisticated and cinematic, with creative typography.”

Strong: “Set a single condensed headline across the upper third; let the subject pass in front of two letters while the remaining letters sit behind the foreground railing. Keep the bottom third free of supporting copy.”

A concept sentence may establish direction; do not let it replace decisions the model actually needs to execute. Avoid reader-experience narration (e.g., “at first glance the viewer discovers ...”): specify the spatial, optical, and typographic arrangement that produces the effect. Do not impose arbitrary numeric precision.

## Step 4 — Respect physical causal chains

If the effect depends on geometry, specify **emitter → physical object → receiving surface → camera** and the relevant viewpoint, occlusion and scale relations.

Be explicit about uncertainty. Numbers are useful when measured or supported by references; invented centimeter-level precision can create contradictions. A reference diagram or controlled compositing workflow may be more reliable than another page of prose.

Examples of intrinsically difficult tasks: many independent objects combining into exact shadows; pixel-precise edits; text-heavy typography; multiple reflections with physically consistent source and viewing direction.

## Step 5 — Prioritize and simplify

- **P0:** the image would fail the user's intent without this.
- **P1:** important to quality or coherent structure.
- **P2:** optional refinements.

Remove duplicated instructions, abandoned aesthetics, subjective praise, repeated P0 lists, and phrases that explain why earlier versions were liked. Do not pin down every cosmetic detail; preserve room for model execution. A smaller coherent prompt is preferable to a longer contradictory one. Before finalizing, check that the visual mechanism can produce an appealing image rather than merely satisfying a complicated concept.

## Step 6 — Delivery and authorization

Deliver the complete copyable prompt as a finished artifact, usually after the user approves the concept. If Route A, remind the user which image to attach. If Route B, no attachment is necessary unless requested.

**Hard gate:** Do not call an image tool merely because the prompt is complete, contains an imperative, or includes a trigger phrase that *the assistant* placed in it. “Ok,” “continue,” “try this,” “converge,” and “write the prompt” do not authorize generation. The **current user request** must explicitly authorize generation/editing, and any user-defined trigger convention must be fulfilled there. An explicitly user-submitted executable prompt with their required trigger qualifies. When in doubt, deliver only the authorized design/prompt work, not a speculative render.

For follow-up edits, rewrite the prompt so that it is independently usable; do not silently carry forward instructions the user rejected.

## Preflight checklist

- Is it clear which route is active and which image, if any, is the edit base?
- Does the prompt implement the **selected**, not merely proposed, concept?
- Are key positions, sizes, overlap and visual hierarchy actionable?
- Are lighting, typography and causal mechanics consistent?
- Are original identity and previously successful elements protected appropriately?
- Has historical commentary been removed?
- Is the task realistically achievable with the host model, or does it require a multi-step/other-tool strategy?
- Did the user explicitly authorize image generation **in the current request**, satisfying their established trigger if any, as distinct from liking a concept or requesting a prompt?
