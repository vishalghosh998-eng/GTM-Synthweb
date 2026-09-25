# Claude Code Instructions — SynthWeb GTM OS

You are operating inside a controlled GTM research repository. Optimize for correctness, traceability, and cost discipline—not for maximum lead count.

Before acting:
- Read `AGENTS.md`.
- Identify the requested campaign and stage.
- Inspect the relevant skill specification.
- Check whether the task requires approval before external API usage.

When researching:
- Prefer first-party public sources and source URLs.
- Record the retrieval date.
- Quote or summarize only what the source supports.
- Label hypotheses explicitly.
- Do not fabricate missing fields.

When writing outreach:
- Use one primary signal.
- Use situation → insight → inquisition.
- Keep the first email concise.
- Do not use unsupported claims or fake familiarity.
- Ask for a low-friction truth check rather than assuming a meeting.

When coding:
- Add tests for parsers, scoring, gates, and schema validation.
- Prefer deterministic functions for normalization and scoring.
- Use idempotent writes and checkpoints.
- Never print secrets.
- Explain any unverified assumption in the run report.

## Workflow Enforcement

Before performing a multi-stage GTM task:

1. Read `AGENTS.md`.
2. Read the relevant `SKILL.md` files.
3. Inspect the prospect record schema at `shared/prospect-record-schema.json`.
4. Identify the current workflow stage.
5. Check whether cost approval is required.
6. Confirm that prerequisite stages have completed.
7. Produce a run plan before executing external research or enrichment.

### Stage discipline

- Do not jump directly from lead discovery to outreach.
- Do not write outreach before evidence extraction, signal classification, qualification, and service-fit review.
- Do not export outreach records before QA, suppression checks, and human approval.
- Do not represent assumptions as facts.
- Use `unknown` when evidence is unavailable.
- Preserve original source data and append new evidence instead of silently overwriting it.
- Record the source URL and retrieval date for externally obtained evidence.
- Record all blocked, failed, skipped, and manually overridden stages.

### Approval discipline

Before any paid API call, enrichment operation, contact lookup, or high-cost model operation:

- Estimate the expected cost.
- Identify the provider and operation.
- Explain the expected output.
- Request explicit operator approval unless an existing approved budget applies.

Before outreach export:

- Validate the prospect record against the schema.
- Confirm that outreach QA passed.
- Confirm that suppression checks passed.
- Confirm human approval is present.
- Report any unresolved uncertainty.
- Stop instead of exporting if any required gate is missing.

### Required run artifacts

Each run should preserve, where applicable:

- `plan.json`
- `approval.json`
- `records.jsonl`
- `events.jsonl`
- `cost.json`
- `report.md`

Every run must be resumable and auditable.
