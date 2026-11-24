"""Decision and user-facing report contracts."""

from enum import StrEnum

from pydantic import BaseModel, Field

from codeopt.models.candidate import Candidate
from codeopt.models.evidence import Evidence


class Decision(StrEnum):
    VERIFIED_IMPROVEMENT = "VERIFIED_IMPROVEMENT"
    UNVERIFIED = "UNVERIFIED"
    REJECTED = "REJECTED"
    NO_IMPROVEMENT = "NO_IMPROVEMENT"
    ERROR = "ERROR"
    TIMEOUT = "TIMEOUT"
    INCONCLUSIVE = "INCONCLUSIVE"


class Report(BaseModel):
    """Evidence-backed outcome returned by every adapter."""

    decision: Decision
    candidate: Candidate | None = None
    evidence: Evidence | None = None
    limitations: list[str] = Field(default_factory=list)
