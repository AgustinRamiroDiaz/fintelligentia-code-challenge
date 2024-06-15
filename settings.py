from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    auth_user: str
    auth_password: str
    auth_account: str

    model_config = SettingsConfigDict(env_file=".env")
