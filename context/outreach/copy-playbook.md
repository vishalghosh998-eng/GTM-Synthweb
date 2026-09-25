# SynthWeb Outreach Copy Playbook

Status: operational draft; requires campaign-owner approval before live use.

## 1. Purpose

Create short, evidence-led outbound messages for SynthWeb's custom software development and engineering-capacity offers. The objective of the first email is a relevant reply, not an immediate meeting.

## 2. Positioning rules

- Lead with the prospect's observable situation, not SynthWeb's capabilities.
- Use one primary signal and one interpretation only.
- Never convert a signal into an unsupported pain claim.
- Describe SynthWeb as a possible route to evaluate, not as the predetermined answer.
- Prefer a useful question over a meeting request.
- Use plain language. Avoid marketing adjectives, generic praise, and tool-stack dumping.
- Do not pretend familiarity, imply prior interaction, or mention private/sensitive data.

## 3. Evidence ladder

1. Direct public statement by the company or executive.
2. Current first-party job posting or company page.
3. Multiple corroborating public sources.
4. One indirect signal.
5. Model hypothesis.

Only levels 1–3 can normally support a personalized claim. Level 4 may support a cautious question. Level 5 must remain internal and cannot be presented as fact.

## 4. Message architecture: Situation → Insight → Inquisition

- Situation: state the verified event in natural language.
- Insight: explain a narrow operational implication, using conditional language where needed.
- Inquisition: ask one low-friction question that lets the recipient correct or confirm the hypothesis.

Template:

> Saw [verified situation]. That can sometimes create [narrow, conditional implication] when [relevant condition]. Is [specific question] something your team is considering, or is the priority elsewhere?

## 5. Signal-to-angle map

| Signal | Safe angle | Do not claim |
|---|---|---|
| Active engineering hiring | Capacity, delivery bandwidth, or hiring-process coordination | They cannot hire or are desperate |
| Multiple similar roles | Team expansion or parallel delivery needs | Hiring failure or urgency |
| Persistent open role | Continued public recruiting activity | The role is hard to fill based on age alone |
| New product/feature page | Possible product delivery workload | Product launch pressure or budget |
| Distributed/contractor language | Existing openness to external delivery models | They want Indian vendors unless stated |
| Specific tech requirement | Relevant technical overlap to explore | Full stack capability unless verified |
| Public engineering pain statement | Directly address the stated issue | Broader organizational problems |

## 6. Email constraints

- First email: 45–75 words by default.
- Follow-up: 25–60 words.
- One CTA and one question.
- One primary signal, maximum one supporting detail.
- No more than one SynthWeb capability mention.
- No links in the first email unless required by the campaign owner.
- No attachments, case-study claims, metrics, pricing, guarantees, or availability claims without approval.
- Do not use fake urgency, false scarcity, or “just checking in.”
- Avoid phrases such as: “I noticed you are struggling,” “quick call,” “synergy,” “revolutionize,” “best-in-class,” and “I know you are busy.”

## 7. CTA library

Use only when supported by the evidence:

- Correction CTA: “Is that relevant to your team, or am I reading the signal incorrectly?”
- Priority CTA: “Is delivery capacity or direct hiring the bigger priority right now?”
- Model CTA: “Are you open to evaluating external engineering capacity for this work?”
- Timing CTA: “Is this an active priority this quarter, or not currently?”
- Routing CTA: “Would this sit with you, or is there someone closer to engineering delivery?”

## 8. Sequence logic

Email 1: verified situation + narrow hypothesis + correction question.

Email 2: add one new evidence item or useful reframing. Do not repeat the first email with synonyms.

Email 3: provide a graceful close, permission-based next step, or routing question. Include opt-out handling where required by the campaign process.

Each email must stand alone. Do not invent a progression such as “following up again” when the recipient has not engaged.

## 9. Personalization hierarchy

1. Company-level operating signal.
2. Role-relevant responsibility.
3. Specific technical or product context.
4. Publicly stated initiative or opinion.

Avoid superficial personalization such as mentioning location, school, generic company praise, or a recent post that has no relationship to the offer.

## 10. Output contract

Every draft must return:

- `subject`
- `body`
- `primary_signal`
- `evidence_urls`
- `hypothesis`
- `cta_type`
- `word_count`
- `risk_flags`
- `review_status`

If evidence is weak, return `needs_more_evidence` rather than writing confident copy.
