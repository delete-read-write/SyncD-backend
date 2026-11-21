from importlib.metadata import version
from typing import Literal

from pydantic import BaseModel

type LoggingLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class ConfigSection(BaseModel):
    pass


class AppSettings(ConfigSection):
    service_name: str = "SyncD"
    service_version: str = version("syncd-backend")


class LoggingSettings(ConfigSection):
    level: LoggingLevel = "INFO"
    fmt: str = (
        "[%(asctime)s.%(msecs)03d] [%(threadName)s] "
        "%(funcName)20s "
        "%(module)s:%(lineno)d "
        "%(levelname)-8s - %(message)s"
    )
    datefmt: str = "%Y-%m-%d %H:%M:%S"


class FastAPISettings(ConfigSection):
    debug: bool = False
    docs_url: str | None = "/docs"
    redoc_url: str | None = "/redoc"
    openapi_url: str | None = "/openapi"
