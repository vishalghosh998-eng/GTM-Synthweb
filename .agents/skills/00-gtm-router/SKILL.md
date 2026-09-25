# 00 GTM Router

## Purpose
Plan a workflow before any expensive action. Estimate scope, providers, stages, and spend.

## Inputs
- Campaign request
- Input source and record count
- ICP configuration
- Available provider credentials
- Approval mode

## Procedure
1. Parse the request into a named campaign.
2. Identify the minimum required stages.
3. Classify each stage as free/local, low-cost, or paid/expensive.
4. Estimate calls, records, model usage, and provider costs.
5. Identify missing credentials and safe skips.
6. Produce a plan and request explicit approval before external spend.

## Output
- `plan.json`
- `approval_required: true` unless the operator has already approved the exact scope and budget.

## Hard rules
- Do not execute downstream paid stages before approval.
- Do not assume provider pricing; use configured pricing or mark cost as unknown.
- Do not hide uncertainty in the estimate.
