from dataclasses import dataclass


@dataclass(frozen=True)
class TestCase:
    input: str
    output: str
