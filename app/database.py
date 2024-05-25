from datetime import date, datetime
from typing import Annotated, Optional, Union
from pydantic_core import Url, MultiHostUrl
import sqlalchemy as sa
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
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


# intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True, index=True)]
# str16 = Annotated[str, 16]
# str128 = Annotated[str, 128]
# str256 = Annotated[str, 256]
# str512 = Annotated[str, 512]
# str1024 = Annotated[str, 1024]


class Base(DeclarativeBase):
    type_annotation_map = {
        # str16: sa.String(16),
        # str128: sa.String(128),
        # str256: sa.String(256),
        # str512: sa.String(512),
        # str1024: sa.String(1024),
        date: sa.Date,
        datetime: sa.DateTime,
    }
