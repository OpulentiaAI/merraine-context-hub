"""Deterministic policy application for judgments returned by TypeSafe."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Outcome = Literal["pass", "fail", "review", "abstain", "unavailable", "refused"]


@dataclass
class Budget:
    """Bound a single run; callers must share one instance across requests."""

    max_calls: int
    max_latency_ms: int
    calls: int = 0
    latency_ms: int = 0

    def reserve_call(self) -> bool:
        if self.calls >= self.max_calls or self.latency_ms >= self.max_latency_ms:
            return False
        self.calls += 1
        return True

    def record_latency(self, elapsed_ms: int) -> bool:
        self.latency_ms += max(0, elapsed_ms)
        return self.latency_ms <= self.max_latency_ms


@dataclass(frozen=True)
class Decision:
    outcome: Outcome
    probability: float | None
    threshold: float
    reason: str
    send: Literal[False] = False


def decide_noul(
    probability: float | None,
    threshold: float,
    *,
    review_lower: float | None = None,
    review_upper: float | None = None,
    available: bool = True,
    abstained: bool = False,
) -> Decision:
    """Apply a threshold as a comparison, never a ranking or magnitude."""
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be between 0 and 1")
    if review_lower is not None or review_upper is not None:
        if review_lower is None or review_upper is None or not 0 <= review_lower <= review_upper <= 1:
            raise ValueError("review band must be two ordered probabilities between 0 and 1")
    if not available:
        return Decision("unavailable", None, threshold, "provider unavailable; deterministic fallback required")
    if abstained:
        return Decision("abstain", probability, threshold, "provider abstained; deterministic fallback required")
    if probability is None or not 0.0 <= probability <= 1.0:
        return Decision("unavailable", probability, threshold, "invalid probability; deterministic fallback required")
    if review_lower is not None and review_lower <= probability <= review_upper:
        return Decision("review", probability, threshold, "probability is in the human-review band")
    if probability >= threshold:
        return Decision("pass", probability, threshold, "probability meets threshold")
    return Decision("fail", probability, threshold, "probability does not meet threshold")
