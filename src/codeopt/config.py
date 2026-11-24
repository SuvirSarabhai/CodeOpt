"""Configuration boundary for CodeOpt providers, limits, and policy."""

from pydantic import BaseModel, Field


class Settings(BaseModel):
    """Application settings shared by adapters and the service layer."""

    minimum_speedup: float = Field(default=1.05, gt=1.0)
    candidate_limit: int = Field(default=3, ge=1)
    default_timeout_seconds: float = Field(default=10.0, gt=0)
