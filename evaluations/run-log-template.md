# Visual Co-Creation — Evaluation Run Log

> Copy once per trial. Written protocol; this file is **not proof of a passed test**. Do not upload user-owned private image assets or chats without consent.

## Setup

- Date / evaluator:
- Task ID / test-case ID:
- Trial number:
- Model / version / provider:
- Host / tool interfaces:
- Condition: `no skill` / `v0.2.0` / `v0.3.0`
- Reference image role(s) and rights (without disclosing private assets):
- Generation budget (allowed calls, actual calls):
- Random seed/configuration if supported:
- Current-user request (redact personal content):
- Previous conversational state (synthetic summary only):

## Observable tool-use record

| Turn | Current user intent | User-defined trigger required? | Trigger present **as active current instruction**? | Image call observed? | Allowed? | Evidence/ref |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

**Critical gate**: no tool call without explicit current execution intent and any user-set trigger. Historical or assistant-written triggers do not count. Audit logs, **not the agent's self-report**, are the evidence.

## Decision-contract audit

- CORE:
- KEEP:
- CHANGE:
- AVOID:
- SOURCE:
- TEXT:
- Was source choice and exact text preserved?
- Any rejected visual mechanism reintroduced?

## Text behavior (0 absent / 1 partial / 2 clear / N/A)

| Measure | Score | Observable evidence |
| --- | --- | --- |
| Accurate source observation | | |
| Specific creative opportunity / novelty | | |
| Builds on user ideas | | |
| Short, constructive dialogue | | |
| Proactive convergence at appropriate time | | |
| Decision preservation | | |
| Prompt correctness / high signal density | | |
| Consent and tool-use behavior | | |

Record repeated questions, invented visual details, or unwanted outputs separately.

## Image evaluation (only if generated)

Record exact generated asset refs and independent comparisons; do not invent a score for an unobserved image.

- **Fidelity** (goal, geometry, text, material): /5, evidence:
- **Aesthetic quality** (composition, coherence, expressive impact): /5, evidence:
- **Preservation** (locked prior strengths): /5, evidence:
- **Side effects / unwanted redesign:**
- **Pairwise human preference** (A/B/blind order, explanation):
- Evaluator 2 disagreement / uncertainty:
- Other model variability notes:

## Judgment and next action

- Critical violation? Y/N and evidence:
- Failure hypothesis: conceptual / design / prompt / stochastic / tool capability / preservation / none
- Proposed change, stop or rollback:
- Unverified assumptions:
- Is this result from a static check, a behavioral tool-log audit, or an actual image/user trial?
