from datetime import date, datetime
from typing import Annotated, Union
from uuid import UUID

import sqlalchemy as sa
from pydantic_core import MultiHostUrl, Url
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, sessionmaker

from app.config import config


class Database:
    def __init__(self, dsn: Union[Url, MultiHostUrl], test_mode: bool = False):
        self._database_dsn = dsn.unicode_string()
        self._test_mode = test_mode

    @property
    def engine(self) -> AsyncEngine | Engine:
        if self._test_mode:
            return create_async_engine(config.database_dsn.unicode_string(), poolclass=sa.NullPool)
        return create_async_engine(config.database_dsn.unicode_string())

    @property
    def async_session(self) -> sessionmaker:
        return sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)


if config.mode == "TEST":
    database = Database(config.database_dsn, test_mode=True)
else:
    database = Database(config.database_dsn)


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True, index=True)]
uuidpk = Annotated[UUID, mapped_column(primary_key=True, index=True, server_default=sa.text("uuid_generate_v4()"))]
str16 = Annotated[str, 16]
str128 = Annotated[str, 128]
str256 = Annotated[str, 256]
str512 = Annotated[str, 512]
str1024 = Annotated[str, 1024]
created_at = Annotated[datetime, mapped_column(server_default=sa.text("timezone('UTC', now())"))]


class Base(DeclarativeBase):
    type_annotation_map = {
        int: sa.Integer,
        str: sa.String,
        str16: sa.String(16),
        str128: sa.String(128),
        str256: sa.String(256),
        str512: sa.String(512),
        str1024: sa.String(1024),
        UUID: sa.UUID,
        date: sa.Date,
        datetime: sa.DateTime,
    }
