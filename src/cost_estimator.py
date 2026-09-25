"""Small deterministic helpers for campaign cost planning."""
from dataclasses import dataclass

@dataclass
class CostEstimate:
    low: float
    high: float
    assumptions: list[str]
    unknowns: list[str]

def estimate_linear(records: int, cost_per_record_low: float|None, cost_per_record_high: float|None) -> CostEstimate:
    assumptions=[]; unknowns=[]
    if cost_per_record_low is None or cost_per_record_high is None:
        unknowns.append("Provider pricing not configured")
        return CostEstimate(0.0, 0.0, assumptions, unknowns)
    assumptions.append(f"{records} records")
    return CostEstimate(records*cost_per_record_low, records*cost_per_record_high, assumptions, unknowns)
