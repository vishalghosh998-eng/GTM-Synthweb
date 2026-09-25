---
name: email-writer
description: Write SynthWeb outbound email copy from an approved evidence packet and sequence plan.
---

# Email Writer

Read these files first:

- `context/outreach/copy-playbook.md`
- `context/company/approved-claims.md`
- `context/compliance/outreach-safety.md`
- `shared/evidence-rules.md`

## Hard requirements

- Write from verified evidence only.
- Use Situation → Insight → Inquisition.
- Use one primary signal and one insight.
- Default to 45–75 words for email 1 and 25–60 for follow-ups.
- Ask one question or make one CTA.
- Avoid generic praise, false familiarity, unsupported pain, budget claims, urgency, and invented technical capability.
- Do not claim that a prospect is struggling to hire merely because a role is open or old.
- If evidence does not support a relevant angle, return `needs_more_evidence`.

## Required output

Return structured JSON with `subject`, `body`, `primary_signal`, `hypothesis`, `evidence_urls`, `cta_type`, `word_count`, `risk_flags`, and `review_status`.
