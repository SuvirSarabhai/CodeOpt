"""Candidate optimization contract."""

from pydantic import BaseModel, Field


class Candidate(BaseModel):
    """A proposed code change; its claims must be verified experimentally."""

    strategy: str
    description: str
    code: str
    assumptions: list[str] = Field(default_factory=list)
    estimated_complexity: str | None = None
    potential_behavior_changes: list[str] = Field(default_factory=list)
