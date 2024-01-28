from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent
DEBUG = False


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=f"{BASE_DIR / '.env'}", extra="ignore")
    debug: bool = Field(default=DEBUG, alias="DEBUG")


class TgBotConfig(BaseConfig):
    token: str = Field(alias="BOT_TOKEN")

    @property
    def get_token(self):
        if self.token:
            return self.token
        raise ValueError("TG_BOT is not set in the .env file")


class Config(BaseSettings):
    tg_bot: TgBotConfig = TgBotConfig()


config = Config()
