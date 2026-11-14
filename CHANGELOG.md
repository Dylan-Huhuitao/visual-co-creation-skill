# Changelog

User-facing changes are summarized here; Git commits track exact file history.

## [0.3.0] — 2026-11-14

### Added

- Explicit intent routing: EXPLORE, DESIGN, PROMPT_ONLY, EXECUTE, CRITIQUE, and REFERENCE_ANALYSIS.
- Visual Opportunity Search and style-as-hypothesis guidance in `references/creative-discovery.md`.
- Compact `CORE / KEEP / CHANGE / AVOID / SOURCE / TEXT` decision contract.
- Prompt Compiler with a high-information-density deletion pass and original-vs-generated-source distinctions.
- Dual-axis Fidelity × Aesthetic Quality evaluation plus preservation and repeat-failure stopping strategy.
- Source/reference role classification and fixed/variable/sample-residue style analysis.
- Eight manual evaluation scenarios E18–E25, an audit run-log template and a static documentation linter.
- CI workflow for deterministic documentation/links/version/case-ID checks.

### Changed

- Shortened `SKILL.md` and moved detailed procedures into references loaded when relevant.
- Preserved adaptive short-turn exploration and two proactive convergence checkpoints without forcing them on complete briefs.
- Clarified that prompt-only, quoted/assistant-written triggers, prior turns, and ambiguous approval are **not** image-tool authorization.
- Protected user-defined visual decisions and successful regions from unintended iterative redesign.
- Updated synthetic examples and README to describe the new request modes and testing limits.

### Evidence and limitations

- **Experimental, unvalidated**: publication of rules and static-check execution does not show that hosts obey authorization or that creative/image quality improved.
- No automatic image rendering, tool-interception hook, model benchmark or proprietary artwork dataset was added.
- No reuse license was selected.

## [0.2.0] — 2026-11-13

### Changed

- Replaced default multi-concept menus with short, interactive, one-idea-at-a-time co-creation.
- Added two adaptive **proactive convergence** checkpoints: concept and execution design; announce the next step before changing stages.
- Expanded style exploration to include unexpected artistic media, materials, and visual mechanisms grounded in the actual image.
- Added an explicit lightweight decision ledger (agreed / tentative / rejected / already successful).
- Strengthened generation consent: vague approval or an assistant-authored trigger inside a draft is never execution authorization.
- Emphasized concise, professional prompts and preservation of style coherence during targeted edits.
- Made humor and emoji user-adaptive rather than mandatory.
- Updated bilingual README, synthetic walkthroughs, and manual evaluation cases E11–E17.

### Validation status

- **Not benchmarked or tested as superior to v0.1.0.** Rules reflect limited qualitative collaboration evidence.
- No image model, runnable test suite, or license was added.

## [0.1.0] — 2026-11-10

### Added

- Initial standards-aligned Agent Skill with an adaptable human–AI visual co-creation workflow.
- Two explicit starting routes: image-led redesign and text-first concept development.
- User concept-selection checkpoint before writing a final prompt.
- Distinct prompt delivery and user-authorized image-generation steps.
- Visual-reference analysis, decision-first prompt construction and targeted revision guidance.
- Synthetic examples illustrating both routes.
- Manual behavioral evaluation cases, including scope protection and authorization.

### Known gaps

- No measured improvement over an agent without the skill.
- Mostly image-led editorial/design experience; text-first route needs practical testing.
- No automatic test runner or model-specific image adapter.
- No chosen reuse license.
