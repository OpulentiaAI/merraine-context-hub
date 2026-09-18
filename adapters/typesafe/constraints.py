"""Deterministic policy application for judgments returned by TypeSafe."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


Outcome = Literal["pass", "fail", "review", "abstain", "unavailable", "refused"]

# The ceiling that bounds spend is policy, so it lives here and not at the call
# site. A caller may ask for a TIGHTER budget; it may not raise the cap.
HARD_MAX_CALLS = 1
HARD_MAX_LATENCY_MS = 2_000


class Budget:
    """Bound a single run. The ceiling is a hard cap, not a default.

    A budget a caller can silently widen is not a budget. The limits are
    read-only after construction, and construction rejects any value above the
    module-level cap, so the evaluated fail-closed ceiling cannot be raised
    from a call site. Lowering it is allowed, including to zero for a caller
    that wants to prove refusal.
    """

    __slots__ = ("_max_calls", "_max_latency_ms", "_calls", "_latency_ms")

    def __init__(self, max_calls: int = HARD_MAX_CALLS,
                 max_latency_ms: int = HARD_MAX_LATENCY_MS) -> None:
        if not isinstance(max_calls, int) or not 0 <= max_calls <= HARD_MAX_CALLS:
            raise ValueError(
                f"max_calls must be an int between 0 and {HARD_MAX_CALLS}; "
                f"got {max_calls!r}. The ceiling is policy and cannot be raised."
            )
        if not isinstance(max_latency_ms, int) or not 0 <= max_latency_ms <= HARD_MAX_LATENCY_MS:
            raise ValueError(
                f"max_latency_ms must be an int between 0 and {HARD_MAX_LATENCY_MS}; "
                f"got {max_latency_ms!r}. The ceiling is policy and cannot be raised."
            )
        self._max_calls = max_calls
        self._max_latency_ms = max_latency_ms
        self._calls = 0
        self._latency_ms = 0

    @property
    def max_calls(self) -> int:
        return self._max_calls

    @property
    def max_latency_ms(self) -> int:
        return self._max_latency_ms

    @property
    def calls(self) -> int:
        return self._calls

    @property
    def latency_ms(self) -> int:
        return self._latency_ms

    def reserve_call(self) -> bool:
        if self._calls >= self._max_calls or self._latency_ms >= self._max_latency_ms:
            return False
        self._calls += 1
        return True

    def record_latency(self, elapsed_ms: int) -> bool:
        self._latency_ms += max(0, elapsed_ms)
        return self._latency_ms <= self._max_latency_ms


@dataclass(frozen=True)
class Decision:
    outcome: Outcome
    probability: float | None
    threshold: float
    reason: str
    send: Literal[False] = field(default=False, init=False)


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
