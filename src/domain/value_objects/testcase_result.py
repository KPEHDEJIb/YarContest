from dataclasses import dataclass


@dataclass(frozen=True)
class TestCaseResult:
    output: str
    error: str | None
    time: int
    exit_code: int
