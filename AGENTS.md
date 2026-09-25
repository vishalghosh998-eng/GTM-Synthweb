# SynthWeb GTM OS — Agent Operating Rules

This repository is an evidence-first outbound GTM system for SynthWeb. Skills under `skills/` are authoritative for their own inputs, outputs, gates, and failure behavior.

## Mandatory execution rules

1. For any multi-step request, start with `skills/00-gtm-router/SKILL.md`.
2. Before any paid API, enrichment, contact lookup, or large model operation, produce a cost estimate and request explicit approval.
3. Never hardcode secrets. Load environment variables from `.env` only through approved scripts.
4. Missing optional credentials must cause a documented skip, not a crash and not a fabricated result.
5. Use `runs/<run-id>/` for all run outputs. Never write runtime data into a skill directory.
6. Read the relevant `SKILL.md` before executing that skill.
7. Preserve source URLs, retrieval timestamps, provider names, and confidence for material claims.
8. Agents may add fields to records but must not silently overwrite source evidence or prior decisions.
9. Unknown is a valid value. Do not convert missing evidence into a positive or negative claim.
10. Every failure must be recorded with stage, error class, retryability, and next action.
11. Start with a small pilot. Default pilot approval target: 50–100 company records, with human review.
12. Do not send outreach automatically unless the operator explicitly changes the approval mode after reviewing pilot results.
13. Never bypass access controls, authentication, CAPTCHAs, robots directives, provider limits, or terms of service.
14. Do not infer protected or sensitive personal characteristics.
15. Do not claim that a prospect has hiring difficulty, budget, turnover, dissatisfaction, or intent unless supported by explicit evidence.
16. Separate observed facts, hypotheses, recommendations, and unknowns in every research dossier.
17. Do not use a job-posting age alone as proof of failed hiring.
18. Before exporting to ReachInbox, run outreach QA and suppression checks.

## Canonical artifacts

- `shared/record-schema.json`: canonical lead record shape
- `shared/evidence-rules.md`: evidence and inference policy
- `shared/conventions.md`: run, checkpoint, and record conventions
- `context/company/approved-claims.md`: permitted SynthWeb claims
- `context/icp/signal-taxonomy.md`: signal definitions and confidence rules

## Mandatory Workflow and Approval Gates

Claude must follow the workflow stages in order unless the operator explicitly authorizes a documented exception.

### Required workflow

1. Router and task classification
2. Cost estimation and approval check
3. Lead intake and normalization
4. Company and contact qualification
5. Evidence extraction
6. Signal classification
7. ICP scoring and service-fit assessment
8. Contact resolution
9. Outreach drafting
10. Outreach QA
11. Suppression and compliance checks
12. Human approval
13. Export to an outreach platform
14. Reply tracking and learning feedback

### Enforcement requirements

- Claude must not skip a required stage silently.
- Every stage must record its status: `not_started`, `in_progress`, `completed`, `blocked`, or `failed`.
- A stage cannot be marked `completed` without its required output.
- A failed or blocked stage must include an error, reason, and next action.
- Records with missing mandatory evidence must not proceed to outreach drafting.
- Records must not be exported to ReachInbox or another outreach platform unless:
  - Required evidence exists.
  - Contact identity has been verified or explicitly marked unknown.
  - Outreach QA has passed.
  - Suppression checks have passed.
  - Human approval has been recorded.
- Claude must never treat a draft as approved merely because it was generated successfully.
- Claude must never send outreach automatically during the pilot phase.
- Approval must be recorded in a run artifact and linked to the relevant record IDs.
- Any manual override must include the operator, timestamp, reason, affected stage, and scope.
- If a required gate cannot be verified, the safe outcome is `blocked`, not `approved`.

### Export gate

The export status must remain `blocked` unless all conditions are true:

- `workflow.qa_status == "passed"`
- `workflow.suppression_status == "passed"`
- `approval.human_approved == true`
- `approval.approver` is present
- `approval.approved_at` is present
- `contact.identity_status == "verified"` or the record is explicitly approved for manual review
- At least one source-backed signal is available
- No unresolved critical errors exist

A record that fails any export condition must not be exported.
