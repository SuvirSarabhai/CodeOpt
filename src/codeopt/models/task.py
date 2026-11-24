"""Optimization task contract."""

from typing import Any

from pydantic import BaseModel, Field


class Task(BaseModel):
    """Code and behavioral constraints evaluated by the pipeline."""

    code: str
    entrypoint: str
    inputs: list[Any] = Field(default_factory=list)
    objective: str = "runtime"
    constraints: dict[str, Any] = Field(default_factory=dict)
