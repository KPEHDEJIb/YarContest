from __future__ import annotations

from src.domain.value_objects import TestCase, TaskId


class Task:
    def __init__(self, task_id: TaskId, title: str, description: str, examples: list[TestCase], tests: list[TestCase]):
        self.id = task_id
        self.title = title
        self.description = description
        self.examples = examples
        self.tests = tests

    @classmethod
    def create(cls, title: str, description: str, examples: list[TestCase], tests: list[TestCase]) -> Task:
        return cls(TaskId.generate(), title=title, description=description, examples=examples, tests=tests)
