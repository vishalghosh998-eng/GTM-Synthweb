# Signal Taxonomy

Each signal must include: signal type, observed claim, source URL, source date if available, retrieved date, confidence, and interpretation limits.

## Signal types

### HIRING_ACTIVE
A relevant role is currently open or recently verified as open.

### HIRING_PERSISTENT
A relevant posting remains open across a measured period. This is a research trigger, not proof of hiring failure.

### HIRING_MULTIPLE
Multiple related engineering vacancies are observed.

### TECH_MATCH
The source explicitly names a technology compatible with verified SynthWeb capability.

### PRODUCT_EXPANSION
A reliable public source indicates product, market, or engineering expansion.

### CONTRACTOR_OR_DISTRIBUTED
The company explicitly mentions contractors, external teams, distributed engineering, or a comparable model.

### EXPLICIT_PAIN
The company or a responsible person explicitly describes a relevant challenge. This is stronger than an inferred pain hypothesis.

## Confidence

- `high`: direct, recent, first-party or highly reliable source.
- `medium`: credible but indirect or partially corroborated evidence.
- `low`: weak, stale, ambiguous, or single-source inference.

## Forbidden inference

Do not infer turnover, inability to hire, budget, dissatisfaction, or urgency from job age, employee count, funding, or a single social post alone.
