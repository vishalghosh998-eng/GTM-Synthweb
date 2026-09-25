# 01 Lead Intake

## Purpose
Normalize input records into the canonical record contract.

## Inputs
CSV, JSONL, or provider output containing at least one company identifier or source URL.

## Procedure
1. Parse using a real CSV/JSON parser.
2. Normalize whitespace, country names, domains, and URLs.
3. Generate stable record IDs.
4. Detect duplicate company-domain-source combinations.
5. Preserve raw input fields.
6. Mark missing required fields without inventing values.

## Output
`records.jsonl` with `workflow.status=received`.

## Failure behavior
Malformed rows are isolated and recorded in `events.jsonl`; valid rows continue.
