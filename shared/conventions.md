# Shared Conventions

## Runs

All execution artifacts live under `runs/<run-id>/`. A run should contain:

- `plan.json`
- `approval.json`
- `records.jsonl`
- `events.jsonl`
- `cost.json`
- `report.md`

## Record handling

- Use stable `record_id` values.
- Preserve raw source references.
- Add fields rather than replacing prior evidence.
- Write checkpoints after each record or safe batch.
- Make stages idempotent.
- Store failures with retryability and next action.

## Status values

`received`, `screened`, `qualified`, `researched`, `scored`, `contact_resolved`, `drafted`, `qa_passed`, `human_approved`, `exported`, `rejected`, `nurture`, `failed`.
