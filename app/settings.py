import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict

curr_dir = pathlib.Path(__file__).parent.resolve()
env_file = curr_dir.parent / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8")

    # Database
    DB_DRIVER_NAME: str
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str


settings = Settings()
