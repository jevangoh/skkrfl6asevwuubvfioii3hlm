from __future__ import annotations

from typing import Any
from uuid import UUID as Uuid, uuid4 as generate_uuid

from sqlmodel import SQLModel as SqlModel, Field


class Model(SqlModel):
    __table_args__ = {"extend_existing": True}
    id: Uuid = Field(primary_key=True, default_factory=generate_uuid)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Model):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)

    def __init__(self, id: Uuid | str | None, **data: Any) -> None:
        if id is None:
            id = generate_uuid()
        elif isinstance(id, str):
            id = Uuid(id)
        super().__init__(id=id, **data)


skkrfl6asevwuubvfioii3hlm = Model
