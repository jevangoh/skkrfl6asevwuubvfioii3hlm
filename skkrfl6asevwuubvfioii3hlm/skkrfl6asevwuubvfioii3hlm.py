from __future__ import annotations

from threading import Event as AwaitEvent
from typing import Annotated, Any
from typing import ClassVar as ClassVariable
from uuid import UUID as Uuid
from uuid import uuid4 as generate_uuid

import sqlalchemy
from pydantic import BeforeValidator, PlainSerializer, WithJsonSchema
from pydantic import PrivateAttr as Private
from sqlmodel import Field
from sqlmodel import SQLModel as SqlModel

type RequestId = Uuid
_unset = sentinel("unset")


class skkrfl6asevwuubvfioii3hlm(SqlModel):
    __table_args__ = {"extend_existing": True}
    default_base_url: ClassVariable[str | None] = None

    id: Annotated[
        Uuid,
        PlainSerializer(
            lambda _value_: _value_ if isinstance(_value_, Uuid) else Uuid(_value_),
            return_type=Uuid,
        ),
        BeforeValidator(lambda _value_: _value_ if isinstance(_value_, Uuid) else Uuid(_value_)),
        WithJsonSchema({"type": str}),
    ] = Field(primary_key=True, sa_type=sqlalchemy.Uuid, default_factory=generate_uuid)

    _active_requests: dict[RequestId, AwaitEvent] = Private(default_factory=dict)
    _base_url: str | None = Private(default=None)

    @property
    def active_requests(self) -> dict[RequestId, AwaitEvent]:
        return self._active_requests

    @active_requests.setter
    def active_requests(self, new_value: dict[RequestId, AwaitEvent]) -> None:
        self._active_requests = new_value

    @property
    def base_url(self) -> str | None:
        return self._base_url

    @base_url.setter
    def base_url(self, new_value: str | None) -> None:
        self._base_url = new_value

    def __init__(
        self, *, id: Uuid | None = None, base_url: str | None = _unset, **data: Any
    ) -> None:
        _init_kwargs_: dict[str, Any] = data.copy()
        if id is not None:
            _init_kwargs_["id"] = id
        super().__init__(**_init_kwargs_)
        self._base_url = self.default_base_url if base_url is _unset else base_url

    def __eq__(self, other: object) -> bool:
        if isinstance(other, skkrfl6asevwuubvfioii3hlm):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)
