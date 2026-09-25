# SynthWeb GTM OS

A controlled, evidence-first GTM research and outreach operating system for SynthWeb. Designed for Claude Code/Codex-style skill execution, with staged qualification, spend gates, resumable records, source provenance, human approval, and ReachInbox handoff.

## Status

**Version:** 0.1 design + implementation scaffold

This repository is not production-ready by default. Before using it for live outreach, verify SynthWeb's current service claims, provider terms, privacy/compliance requirements, sender-domain configuration, and internal approval policy.

## Design principles

1. Signal before personalization.
2. Evidence before inference.
3. Cheap screening before expensive research.
4. No API spend without an estimate and explicit approval.
5. Additive, provenance-preserving records.
6. Human approval before sending during the pilot.
7. Never invent pain, budget, technology, employment status, or personal details.
8. Every result must be resumable, auditable, and explainable.

## Quick start

```bash
cp .env.example .env
python -m venv .venv
# activate the environment
pip install -r requirements.txt
python -m pytest
```

Read `AGENTS.md` and `context/company/approved-claims.md` before running a campaign.

## Operating flow

`router -> intake -> qualification -> extraction -> signals -> judgment -> contact resolution -> email writer -> outreach QA -> human approval -> ReachInbox export -> reply triage`

## Non-goals

- Bypassing platform access controls, login walls, CAPTCHAs, or rate limits.
- Scraping private data.
- Automatically sending unreviewed cold outreach during the pilot.
- Treating inferred pain as confirmed fact.
- Replacing provider terms, legal review, or internal commercial verification.
