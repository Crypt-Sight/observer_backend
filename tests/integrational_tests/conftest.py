import json

import pytest
import sqlalchemy as sa

# from app.config import config

# @pytest.fixture(scope="session", autouse=True)
# async def prepare_database():
#     """Database Setup for test environment"""
#
#     assert config.MODE == "TEST"
#
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#     def open_mock_json(model: str):
#         with open(f"tests/integration_tests/mocks/{model}.json") as mock:
#             return json.load(mock)
#
#     proxy = open_mock_json("proxy")
#     server = open_mock_json("server")
#     artist = open_mock_json("artist")
#     folder = open_mock_json("folder")
#     content = open_mock_json("content")
#
#     async with async_session() as session:
#         statements = [
#             sa.insert(ProxyModel).values(proxy),
#             sa.insert(ServerModel).values(server),
#             sa.insert(ArtistModel).values(artist),
#             sa.insert(FolderModel).values(folder),
#             sa.insert(ContentModel).values(content),
#         ]
#         for statement in statements:
#             await session.execute(statement)
#         await session.commit()
