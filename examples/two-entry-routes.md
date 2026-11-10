# Synthetic Walkthroughs: Both Entry Routes

These are **fictional demonstrations** of expected agent behavior. No images were generated or evaluated for these examples. They are not copies of private user chats.

## Route A — Photograph supplied, editing idea optional

**User input:** A photo of a quiet public-library stairwell with a zigzag steel handrail and late-afternoon sunlight. “Make this feel like an unusual editorial poster.”

**Analysis (observation):** The railing creates a repeated diagonal; the stair treads create horizontal rhythm; sunlight casts long shadows; the top landing has negative space.

**Possible concepts:**

- **A / Folded Path:** The railing shadow becomes a continuous drawn path through a restrained headline. Main mechanism: one existing diagonal links physical architecture and type.
- **B / Split Exposure:** The stairwell is visually separated into two overlapping time-of-day exposures. Main mechanism: the same geometry with two lighting states.
- **C / Stair Atlas:** Step edges become a measured editorial grid with small labels. Main mechanism: architectural repetition as information architecture.

These options differ in mechanism, not merely palette.

**User:** “Choose A, but keep the space natural and use only one major title.”

**Concept locked:** One editorial headline interacts with the physical railing and its cast shadow. Preserve the stairwell's architecture and camera perspective. No extra people or elaborate collage.

**Final editing prompt (example):**

> Edit the attached library stairwell photograph into a vertical editorial poster. Keep the original stair geometry, handrail, concrete texture, late-afternoon light and camera viewpoint. Place a single large condensed title, “BETWEEN FLOORS,” in the upper landing's negative space. Integrate the title spatially with the existing diagonal rail: one letter is partially occluded by the rail while the rail's shadow continues across the title area. Use soft off-white lettering and preserve the source photo's natural color. Maintain readable perspective and a clear viewing hierarchy: architectural diagonal first, title second, stair rhythm third. Do not add people, secondary headlines, new structures, decorative icons or unrelated graphic textures.

**Execution checkpoint:** The agent delivers the prompt. The user reviews/copies it and explicitly submits it with the original image when they wish to generate. The prompt itself is not an execution request.

**Evaluation sketch:** Check title legibility, rail occlusion, source preservation and whether the diagonal relationship really works. A fake floating title is a conceptual failure even if the poster is attractive.

## Route B — Only an initial idea, no source image

**User input:** “I want to create an image about a city starting to breathe again after the rain. I don't have a reference photo.”

**Brief:** City after rainfall, transition toward openness; the user has not fixed medium, time of day, typography or visual density. Do not pretend to inspect a nonexistent image.

**Possible concepts:**

- **A / Exhale:** A street perspective opens from a compressed dark foreground into a wide, luminous sky. Mechanism: spatial expansion.
- **B / Waterline Letters:** The words “AFTER RAIN” emerge only through discontinuous reflected lettering on wet pavement. Mechanism: typography recovered from reflection.
- **C / Stillness in Motion:** Streaked traffic traces contrast with one perfectly still puddle reflecting an unbroken sky. Mechanism: temporal contrast.

**User:** “Choose C. No text and no people. Make it photographic, not a surreal illustration.”

**Concept locked:** A photographic street with motion-streaked passing traffic in the distance, one undisturbed reflective puddle in the foreground, no human figures or added typography.

**Final text-to-image prompt (example):**

> Create a vertical 3:4 photorealistic photograph of a city street just after rainfall, viewed from a low but natural sidewalk perspective at blue hour. The background carries slender horizontal vehicle light trails, while one shallow foreground puddle remains perfectly still and reflects an unobstructed patch of pale evening sky. Use the contrast between motion in the street and stillness in the puddle as the sole organizing idea. Make the puddle the first focal point, light trails the second, and subdued architecture the supporting context. Keep the paving materials, water reflection and atmospheric haze physically believable. Use deep blue-gray shadows with restrained amber highlights. No people, captions, poster typography, collage elements or surreal objects.

**Execution checkpoint:** The agent delivers the prompt. The user explicitly submits it for generation **without attaching an imaginary source image**.

**Evaluation sketch:** The puddle must clearly feel still relative to traffic. If both are blurred, the selected contrast fails. If the model adds an unrelated dramatic figure, the user constraint fails.

## What these two routes demonstrate

- Route A begins with **observed visual structure** and protects the source.
- Route B begins with a **textual creative seed** and does not invent a reference.
- Both create meaningful alternatives before finalizing a concept, then converge on a concrete prompt.
- Neither path requires revealing private reasoning or publishing iterative chat logs.
- Neither example claims that the image model will reliably achieve the prompt.
