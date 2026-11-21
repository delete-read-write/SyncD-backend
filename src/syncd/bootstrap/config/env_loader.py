from pydantic_settings import BaseSettings, SettingsConfigDict

from syncd.bootstrap.config.settings import AppSettings, FastAPISettings, LoggingSettings


class BaseEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


class AppEnvSettings(BaseEnvSettings, AppSettings):  # pyright: ignore[reportIncompatibleVariableOverride]
    model_config = SettingsConfigDict(env_prefix="APP_")


class LoggingEnvSettings(BaseEnvSettings, LoggingSettings):  # pyright: ignore[reportIncompatibleVariableOverride]
    model_config = SettingsConfigDict(env_prefix="LOGGING_")


class FastAPIEnvSettings(BaseEnvSettings, FastAPISettings):  # pyright: ignore[reportIncompatibleVariableOverride]
    model_config = SettingsConfigDict(env_prefix="FASTAPI_")


def _load_env[E: BaseEnvSettings](env_cls: type[E]) -> E:
    return env_cls()


def load_app_settings() -> AppSettings:
    return _load_env(AppEnvSettings)


def load_logging_settings() -> LoggingSettings:
    return _load_env(LoggingEnvSettings)


def load_fastapi_settings() -> FastAPISettings:
    return _load_env(FastAPIEnvSettings)
