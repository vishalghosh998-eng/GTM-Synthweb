---
name: outreach-qa
description: Audit SynthWeb outbound copy before any ReachInbox export.
---

# Outreach QA

Fail the draft if any condition is true:

- The primary signal lacks a source URL.
- The email states an inference as a fact.
- It claims pain, urgency, budget, hiring failure, dissatisfaction, or intent without direct evidence.
- It uses more than one primary signal.
- It exceeds the campaign word limit.
- It contains generic praise, fake familiarity, vague meeting-first CTA, or unsupported service claims.
- The company and contact do not match.
- The contact is suppressed, opted out, unverified, or outside the approved campaign scope.
- It includes sensitive personal information or information obtained through disallowed means.

Return `pass`, `fail`, or `human_review`, with each finding tied to a field or sentence. QA pass is required before export, and pilot campaigns remain human-approved and manually sent.
