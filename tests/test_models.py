from codeopt.models import Candidate, Decision, Report, Task


def test_core_contracts_construct() -> None:
    task = Task(code="def identity(value): return value", entrypoint="identity")
    candidate = Candidate(
        strategy="identity",
        description="No-op candidate used to validate the contract.",
        code=task.code,
    )
    report = Report(decision=Decision.NO_IMPROVEMENT, candidate=candidate)

    assert task.entrypoint == "identity"
    assert report.decision is Decision.NO_IMPROVEMENT
