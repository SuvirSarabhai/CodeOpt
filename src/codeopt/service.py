"""Adapter-independent orchestration entry point."""

from codeopt.models import Report, Task


def optimize(task: Task, budget: int) -> Report:
    """Optimize a trusted task once the pipeline is implemented.

    This signature is frozen at checkpoint C0. The implementation will coordinate
    candidate generation, verification, benchmarking, and decision making.
    """
    raise NotImplementedError("The optimization pipeline is not implemented yet.")
