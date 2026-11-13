# Synthetic Walkthroughs: Brief Dialogue, Two Entry Routes

**Fictional examples only.** No images were generated or benchmarked. These do not reproduce private chats.

## Route A — Source photo, exploration to two convergences

**User:** [Photo of a rainy tram stop with one bright umbrella.] “Can we make an unusual poster?”

**Assistant:** “The umbrella is the only clean circle among all those straight wet rails. What if its reflection became a second, impossible umbrella beneath the pavement—like a small opening to another weather system? Interesting, or too surreal?”

**User:** “Interesting, but I want to keep the photographic mood. Maybe only the reflection changes.”

**Assistant:** “Yes: leave the real umbrella untouched; let the reflection reveal a bright summer sky instead of the gray station. The contrast can stay subtle. I think the concept is ready; we can now settle its placement and whether to use text.”

**User:** “No text. Keep it minimal.”

**Assistant:** “Design convergence: preserve the entire rainy station and umbrella; modify only the puddle reflection with a physically aligned alternate sky; keep everything else subdued. I'll turn that into a complete edit prompt when you ask.”

**User:** “Write the prompt.”

**Assistant (prompt only, no render):** “Edit the attached rainy tram-stop photograph. Preserve the framing, rails, umbrella, wet pavement, pedestrians and overcast lighting. In the puddle directly beneath the umbrella, replace only the reflected gray sky with a small reflection of bright summer-blue sky and softly lit clouds. Match the puddle's viewing angle, ripple distortion, border and wet-surface reflections; the real sky above remains overcast. Keep the effect limited to the puddle. No typography, other surreal elements, frame or watermark.”

**User:** “Ok.”

**Assistant:** Discusses the prompt or next action **without generating**, because “Ok” is not an explicit execution request.

**Later:** If the user explicitly submits the prompt with the required generation authorization, the agent may invoke the image tool.

## Route B — Text-first concept without a photo

**User:** “I want an image about a quiet library at midnight. No photo.”

**Assistant:** “What if the only visible light came from the spaces between closed books, turning the shelves into a softly glowing city skyline? It could be dreamy without using characters. Does that interest you?”

**User:** “Yes. Paper cutouts, not photorealism.”

**Assistant:** “Then we have the core: a midnight library made from deep-blue layered paper; warm windows are narrow gaps between book spines. Concept is settled. I suggest one more decision about viewing angle, then I'll summarize the construction.”

**User:** “Straight on.”

**Assistant:** “Design convergence: frontal shelves as a paper skyline, dark indigo layers, warm light from irregular spine gaps, no humans or text. Ready for a prompt.”

**When asked for the prompt:** Write a self-contained **text-to-image** prompt. Do not claim a source image exists; do not generate until authorized.

## What these examples test

- One image-specific or brief-specific visual move per conversational turn, not an unsolicited menu.
- User feedback actually changes the concept, and the agent proactively marks both convergence points.
- Few impactful decisions, concise executable prompts, and permission to switch approaches.
- Prompt drafting, user approval, and **user-authorized generation** remain separate.
