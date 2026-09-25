---
name: sequence-planner
description: Plan an evidence-led three-email outbound sequence for a SynthWeb campaign.
---

# Sequence Planner

## Inputs

- Approved campaign brief
- Prospect evidence packet
- Selected service hypothesis
- Outreach playbook
- Compliance and suppression status

## Procedure

1. Confirm the prospect, company, role, geography, and source freshness.
2. Select one primary signal. Reject signal stacking that obscures the message.
3. Define the internal hypothesis separately from the external wording.
4. Choose a sequence objective: correction, priority discovery, model fit, routing, or timing.
5. Plan three distinct emails:
   - Email 1: situation, narrow implication, low-friction question.
   - Email 2: new evidence or useful contrast; no paraphrased repetition.
   - Email 3: permission-based close or routing question.
6. Apply word limits, approved claims, suppression checks, and risk flags.
7. Route ambiguous or high-value prospects to human review.

## Required output

Return a sequence plan before copy generation with `primary_signal`, `hypothesis`, `objective`, `email_1_angle`, `email_2_angle`, `email_3_angle`, `evidence_urls`, `unknowns`, and `review_status`.

Never infer budget, urgency, hiring failure, dissatisfaction, or intent from a job posting's age, funding, headcount, or one social post.
