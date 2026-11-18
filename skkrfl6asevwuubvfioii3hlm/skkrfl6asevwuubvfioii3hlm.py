from __future__ import annotations

from typing import Annotated
from uuid import UUID as Uuid
from uuid import uuid4 as generate_uuid

import sqlalchemy
from pydantic import BeforeValidator, PlainSerializer, WithJsonSchema
from pydantic import PrivateAttr as Private
from PySide6.QtCore import QObject, Signal
from sqlmodel import Field
from sqlmodel import SQLModel as SqlModel

type RequestId = Uuid
_unset = sentinel("unset")


class _DeletedSignal(QObject):
    emitted = Signal()


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

    _deleted_signal: _DeletedSignal = Private(default_factory=_DeletedSignal)

    @property
    def deleted_signal(self) -> _DeletedSignal:
        return self._deleted_signal

    def __eq__(self, other: object) -> bool:
        if isinstance(other, skkrfl6asevwuubvfioii3hlm):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)

    def delete(self) -> None:
        pass
