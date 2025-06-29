from __future__ import annotations

import os
import subprocess
import sys
import time
from typing import Any

from src.domain.entities.task import Task
from src.domain.value_objects import SolutionId, TestCaseResult, TestCase


class Solution:
    def __init__(self, solution_id: SolutionId, task: Task, user: Any, code: str):
        self.id = solution_id
        self.task = task
        self.user = user
        self.code = code

    def full_test(self) -> list[TestCaseResult]:  # пока непонятно, что возвращать
        ...

    def _single_test(self, testcase: TestCase) -> TestCaseResult:
        temp_file = f'temp_{time.time()}.py'

        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(self.code)

        result = TestCaseResult('', '', None, 0)
        try:
            start_time = time.time()
            process = subprocess.Popen(
                [sys.executable, temp_file],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                encoding='utf-8'
            )

            try:
                stdout, stderr = process.communicate(
                    input=testcase.input,
                    timeout=testcase.time_limit
                )
                result.time = time.time() - start_time
                result.output = stdout.strip()
                result.error = stderr.strip()
                result.exit_code = process.returncode
            except subprocess.TimeoutExpired:
                process.kill()
                result.error = 'Time limit exceeded'
        except Exception as e:
            result.error = str(e)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

        return result

    @classmethod
    def create(cls, task: Task, user: Any, code: str) -> Solution:
        return cls(SolutionId.generate(), task=task, user=user, code=code)
