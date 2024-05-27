from typing import Any, Dict, List, Optional

from loguru import logger
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError

from app.database import database
from app.exc import DatabaseErrorExc

async_session = database.async_session


class BaseDAO:
    model = None

    @classmethod
    async def add_one(cls, **kwargs) -> int:
        query = insert(cls.model).values(**kwargs)
        async with database.async_session() as session:
            try:
                result = await session.execute(query)
                await session.commit()
                return result.inserted_primary_key[0]
            except IntegrityError as e:
                await session.rollback()
                logger.error(e)
                raise DatabaseErrorExc

    @classmethod
    async def update(cls, values: Dict[str, Any], **filter_by):
        query = update(cls.model).values(**values).filter_by(**filter_by)
        async with database.async_session() as session:
            try:
                await session.execute(query)
                await session.commit()
            except IntegrityError as e:
                await session.rollback()
                logger.error(e)
                raise DatabaseErrorExc

    @classmethod
    async def delete(cls, **filter_by):
        query = delete(cls.model).filter_by(**filter_by)
        async with database.async_session() as session:
            try:
                await session.execute(query)
                await session.commit()
            except IntegrityError as e:
                await session.rollback()
                logger.error(e)
                raise DatabaseErrorExc

    @classmethod
    async def find_all(cls, limit: Optional[int] = None, offset: Optional[int] = None, **filter_by) -> List:
        query = select(cls.model).filter_by(**filter_by)
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)

        async with database.async_session() as session:
            try:
                result = await session.execute(query)
                return result.scalars().all()
            except IntegrityError as e:
                logger.error(e)
                raise DatabaseErrorExc

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with database.async_session() as session:
            try:
                query = select(cls.model).filter_by(**filter_by)
                result = await session.execute(query)
                return result.scalar_one_or_none()
            except IntegrityError as e:
                logger.error(e)
                raise DatabaseErrorExc
