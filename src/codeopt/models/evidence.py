"""Verification and benchmark evidence contract."""

from typing import Any

from pydantic import BaseModel, Field


class Evidence(BaseModel):
    """Measured facts used by the decision engine."""

    verification_passed: bool = False
    inputs_checked: int = 0
    original_median_seconds: float | None = None
    candidate_median_seconds: float | None = None
    speedup: float | None = None
    peak_memory_bytes: int | None = None
    environment: dict[str, Any] = Field(default_factory=dict)
    notes: list[str] = Field(default_factory=list)
