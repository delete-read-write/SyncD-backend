from importlib.metadata import version

from pydantic import BaseModel


class ConfigSection(BaseModel):
    pass


class AppSettings(ConfigSection):
    service_name: str = "SyncD"
    service_version: str = version("syncd-backend")
