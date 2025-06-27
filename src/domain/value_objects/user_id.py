from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class UserId:
    value: UUID

    @classmethod
    def generate(cls):
        return cls(value=uuid4())