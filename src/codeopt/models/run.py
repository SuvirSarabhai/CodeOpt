"""Raw runner output contract."""

from typing import Any

from pydantic import BaseModel


class RunResult(BaseModel):
    """Result from one isolated invocation of an entry point."""

    value: Any | None = None
    value_type: str | None = None
    exception_type: str | None = None
    exception_message: str | None = None
    duration_seconds: float | None = None
    timed_out: bool = False
