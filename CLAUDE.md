# Claude Code Instructions — SynthWeb GTM OS

You are operating inside a controlled GTM research repository. Optimize for correctness, traceability, and cost discipline—not for maximum lead count.

Before acting:
- Read `AGENTS.md`.
- Identify the requested campaign and stage.
- Inspect the relevant skill specification.
- Check whether the task requires approval before external API usage.

When researching:
- Prefer first-party public sources and source URLs.
- Record the retrieval date.
- Quote or summarize only what the source supports.
- Label hypotheses explicitly.
- Do not fabricate missing fields.

When writing outreach:
- Use one primary signal.
- Use situation → insight → inquisition.
- Keep the first email concise.
- Do not use unsupported claims or fake familiarity.
- Ask for a low-friction truth check rather than assuming a meeting.

When coding:
- Add tests for parsers, scoring, gates, and schema validation.
- Prefer deterministic functions for normalization and scoring.
- Use idempotent writes and checkpoints.
- Never print secrets.
- Explain any unverified assumption in the run report.
