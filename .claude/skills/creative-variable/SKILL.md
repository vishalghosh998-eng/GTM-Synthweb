---
name: creative-variable
description: Define safe, source-backed personalization variables for SynthWeb outreach.
---

# Creative Variable

For each campaign, define only variables that can be populated from verified evidence:

- `company_name`
- `recipient_name`
- `recipient_role`
- `primary_signal`
- `signal_date`
- `signal_source_url`
- `relevant_technology`
- `public_initiative`
- `service_hypothesis`
- `cta_type`

For every variable specify: source type, extraction rule, fallback, confidence, and whether human approval is required.

Fallback behavior:

- If a name is unverified, use a role-safe greeting or omit the name.
- If the signal is stale, downgrade confidence and avoid time-sensitive language.
- If a variable is missing, remove the sentence rather than inserting generic filler.
- Never generate personal details, guessed email addresses, inferred pain, or fabricated familiarity.
