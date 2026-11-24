"""Stable domain contracts shared across CodeOpt layers."""

from codeopt.models.candidate import Candidate
from codeopt.models.evidence import Evidence
from codeopt.models.report import Decision, Report
from codeopt.models.run import RunResult
from codeopt.models.task import Task

__all__ = ["Candidate", "Decision", "Evidence", "Report", "RunResult", "Task"]
