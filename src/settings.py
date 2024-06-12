from dataclasses import dataclass
from functools import lru_cache

from pydantic_settings import BaseSettings as PydanticSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")


class BotSettings(BaseSettings):
    NAME: str
    API_ID: str
    API_HASH: str
    PHONE_NUMBER: str | None


class ProducerSettings(BaseSettings):
    PRODUCER_HOST: str
    PRODUCER_PORT: int
    VIRTUAL_HOST: str = '/'
    PRODUCER_USERNAME: str
    PRODUCER_PASSWORD: str
    QUEUE_NAME: str


@dataclass
class Config:
    producer_settings: ProducerSettings
    bot_settings: BotSettings


@lru_cache
def get_config():
    return Config(
        producer_settings=ProducerSettings(),
        bot_settings=BotSettings()
    )
