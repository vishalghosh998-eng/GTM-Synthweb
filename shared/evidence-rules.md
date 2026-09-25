# Evidence Rules

Every material claim must be classified as one of:

- `observed_fact`: directly supported by a source.
- `calculated_fact`: deterministically calculated from observed facts.
- `hypothesis`: plausible interpretation requiring uncertainty language.
- `recommendation`: agent-generated next step.
- `unknown`: insufficient evidence.

Each evidence item should include:

```json
{
  "claim": "...",
  "classification": "observed_fact",
  "source_url": "...",
  "source_published_at": null,
  "retrieved_at": "...",
  "confidence": "high",
  "notes": "..."
}
```

The writing agent may use observed facts and carefully worded hypotheses. It must not turn unknowns into facts.
