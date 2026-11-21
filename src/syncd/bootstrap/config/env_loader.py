from pydantic_settings import BaseSettings, SettingsConfigDict

from syncd.bootstrap.config.settings import AppSettings


class BaseEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


class AppEnvSettings(BaseEnvSettings, AppSettings):  # pyright: ignore[reportIncompatibleVariableOverride]
    model_config = SettingsConfigDict(env_prefix="APP_")


def _load_env[E: BaseEnvSettings](env_cls: type[E]) -> E:
    return env_cls()


def load_app_settings() -> AppSettings:
    return _load_env(AppEnvSettings)
