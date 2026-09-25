"""Deterministic scoring helpers. Unknown values must not receive positive points."""

def score_dimensions(values: dict[str, int|None], weights: dict[str, int]) -> int:
    total=0
    for key, weight in weights.items():
        value=values.get(key)
        if value is None:
            continue
        if not 0 <= value <= 100:
            raise ValueError(f"{key} must be 0..100")
        total += round(weight * value / 100)
    return total
