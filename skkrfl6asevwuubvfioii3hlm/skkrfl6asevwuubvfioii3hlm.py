from __future__ import annotations

from typing import Any, Annotated
from uuid import UUID as Uuid, uuid4 as generate_uuid

from sqlmodel import SQLModel as SqlModel, Field
import sqlalchemy

from pydantic import PlainSerializer, BeforeValidator, WithJsonSchema


class skkrfl6asevwuubvfioii3hlm(SqlModel):
    __table_args__ = {"extend_existing": True}

    id: Annotated[
        Uuid,
        PlainSerializer(
            lambda _value_: _value_ if isinstance(_value_, Uuid) else Uuid(_value_),
            return_type=Uuid,
        ),
        BeforeValidator(lambda _value_: _value_ if isinstance(_value_, Uuid) else Uuid(_value_)),
        WithJsonSchema({"type": str}),
    ] = Field(primary_key=True, sa_type=sqlalchemy.Uuid, default_factory=generate_uuid)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, skkrfl6asevwuubvfioii3hlm):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)
