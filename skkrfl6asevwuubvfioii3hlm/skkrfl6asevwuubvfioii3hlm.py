from __future__ import annotations

from typing import Any, Annotated, TypeAlias, Optional
from uuid import UUID as Uuid, uuid4 as generate_uuid
from threading import Event as AwaitEvent

from sqlmodel import SQLModel as SqlModel, Field
from pydantic import PlainSerializer, BeforeValidator, WithJsonSchema, PrivateAttr as Private
import sqlalchemy

RequestId: TypeAlias = Uuid


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

    _active_requests: dict[RequestId, AwaitEvent] = Private(default_factory=dict)
    _base_url: Optional[str] = Private(default=None)

    @property
    def active_requests(self) -> dict[RequestId, AwaitEvent]:
        return self._active_requests

    @active_requests.setter
    def active_requests(self, new_value: dict[RequestId, AwaitEvent]) -> None:
        self._active_requests = new_value

    @property
    def base_url(self) -> Optional[str]:
        return self._base_url

    @base_url.setter
    def base_url(self, new_value: Optional[str]) -> None:
        self._base_url = new_value

    def __init__(
        self, *, id: Optional[Uuid] = None, base_url: Optional[str] = None, **data: Any
    ) -> None:
        self._base_url = base_url
        _init_kwargs_: dict[str, Any] = data.copy()
        if id is not None:
            _init_kwargs_["id"] = id
        super().__init__(**_init_kwargs_)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, skkrfl6asevwuubvfioii3hlm):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)
