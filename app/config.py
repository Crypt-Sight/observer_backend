import os
from typing import Literal

from pydantic import AmqpDsn, Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

dir_path = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(dir_path, "../.env")
model_config = SettingsConfigDict(env_file=env_path, env_file_encoding="utf-8")


class Config(BaseSettings):
    model_config = model_config

    MODE: Literal["DEV", "PROD", "TEST"]

    API_TOKEN: str

    DB_HOST: str
    DB_PORT: int = Field(default=5432)
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    AMQP_DSN: AmqpDsn

    @property
    def mode(self) -> Literal["DEV", "PROD", "TEST"]:
        return self.MODE

    @property
    def database_dsn(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            host=self.DB_HOST,
            port=self.DB_PORT,
            username=self.DB_USER,
            password=self.DB_PASS,
        )

    @property
    def amqp_dsn(self) -> AmqpDsn:
        return self.AMQP_DSN


config = Config()
