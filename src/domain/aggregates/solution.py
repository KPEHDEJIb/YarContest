from __future__ import annotations

from typing import Any

from src.domain.entities.task import Task
from src.domain.value_objects import SolutionId, TestCaseResult


class Solution:
    def __init__(self, solution_id: SolutionId, task: Task, user: Any, code: str):
        self.id = solution_id
        self.task = task
        self.user = user
        self.code = code

    def test(self) -> list[TestCaseResult]:  # пока непонятно, что возвращать
        ...

    @classmethod
    def create(cls, task: Task, user: Any, code: str) -> Solution:
        return cls(SolutionId.generate(), task=task, user=user, code=code)
