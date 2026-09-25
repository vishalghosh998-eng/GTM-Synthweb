# 05 Judgment and Service Fit

## Purpose
Combine structured evidence into an explainable fit assessment.

## Procedure
1. Score each dimension using `config/scoring.yaml`.
2. Treat unknowns as zero, not as positive evidence.
3. Recommend a service only when evidence matches the service rules.
4. List fit reasons, gaps, unknowns, and disqualifiers.
5. Route uncertain or high-value records to human review.

## Output
- Score and confidence
- Recommended offer
- Evidence-backed reasons
- Unknowns and risks
- Recommended contact roles
