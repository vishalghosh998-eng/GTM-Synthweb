# Campaign Brief Skill

## Purpose

Create a structured, evidence-first campaign brief before lead sourcing or enrichment begins. The brief defines what the GTM run is trying to find, what evidence qualifies a record, what is excluded, and what spend is permitted.

This skill does not source leads, enrich contacts, send outreach, or approve spend.

## When to run

Run after the GTM router classifies a campaign and before lead intake/sourcing.

## Inputs

- Campaign objective
- Target geography
- Target company/customer profile
- Target buyer roles
- Required and preferred signals
- Service or offer being evaluated
- Explicit exclusions/suppression criteria
- Input source, if already available
- Record limit or pilot size
- Available providers and credentials
- Approval mode and budget, if already approved

## Required output

Write a campaign brief containing:

- campaign_id
- objective
- target_market
- buyer_roles
- required_signals
- preferred_signals
- exclusions
- service_fit_questions
- evidence_requirements
- research_scope
- pilot_scope
- budget
- approval_status
- open_questions

Each signal must have:
- a definition,
- acceptable evidence,
- disallowed inference,
- minimum confidence.

## Procedure

1. Name the campaign using a stable, human-readable identifier.
2. Convert the request into observable company-level criteria.
3. Separate required signals from preferred signals.
4. Define exclusions before sourcing begins.
5. Define what evidence is sufficient to call a signal present.
6. Define what must remain unknown.
7. Define the minimum research needed to decide whether a company is worth advancing.
8. Set a pilot record limit before external enrichment.
9. Estimate expected provider/API usage through the router.
10. Require explicit approval before paid work when the router says approval is required.
11. Save the brief as a run artifact before downstream execution.

## Evidence rules

- Do not use job-posting age alone to claim hiring difficulty.
- Do not infer budget, urgency, dissatisfaction, turnover, intent, or contractor preference without evidence.
- Publicly stated technology is evidence of technology use; it is not by itself evidence of a buying need.
- A funding event is context, not proof of hiring need or software demand.
- Separate observed facts, hypotheses, recommendations, and unknowns.
- Preserve source URL, retrieval timestamp, provider, and confidence for material claims.

## Cost rules

- Campaign-brief creation should use local/free computation where possible.
- Do not call paid enrichment or contact providers from this skill.
- If the brief requires external research to answer a campaign question, stop and return the research requirement to the router instead of silently spending.

## Failure behavior

If required campaign inputs are missing:
- mark the brief blocked,
- list the missing fields,
- do not invent values,
- do not start downstream sourcing.

If the scope is contradictory:
- record the contradiction in open_questions,
- do not silently choose one interpretation.

## Completion gate

A campaign brief is completed only when:
- objective is defined,
- target market is defined,
- required/preferred signals are defined,
- exclusions are defined,
- evidence requirements are defined,
- pilot scope is defined,
- approval status is explicit,
- open questions are recorded.

## Handoff

The next stage may use the brief to constrain lead intake, qualification, evidence extraction, signal detection, scoring, and outreach. The brief does not override the repository's global rules in AGENTS.md.
