from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


def _load_env[E: BaseEnvSettings](env_cls: type[E]) -> E:
    return env_cls()
