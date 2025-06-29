from dataclasses import dataclass
from time import time

@dataclass()
class TestCaseResult:
    output: str
    error: str | None
    time: time
    exit_code: int
