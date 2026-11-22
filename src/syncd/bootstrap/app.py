import uvicorn
from fastapi import FastAPI

from syncd.bootstrap.config.env_loader import (
    load_app_settings,
    load_fastapi_settings,
    load_logging_settings,
)
from syncd.bootstrap.config.settings import AppSettings, FastAPISettings, LoggingSettings
from syncd.bootstrap.setup import setup_logging


def make_app(
    app_settings: AppSettings | None = None,
    logging_settings: LoggingSettings | None = None,
    fastapi_settings: FastAPISettings | None = None,
) -> FastAPI:
    logging_settings = logging_settings or load_logging_settings()
    setup_logging(settings=logging_settings)

    app_settings = app_settings or load_app_settings()
    fastapi_settings = fastapi_settings or load_fastapi_settings()

    app = FastAPI(
        debug=fastapi_settings.debug,
        title=app_settings.service_name,
        version=app_settings.service_version,
        docs_url=fastapi_settings.docs_url,
        redoc_url=fastapi_settings.redoc_url,
        openapi_url=fastapi_settings.openapi_url,
    )

    return app


if __name__ == "__main__":
    uvicorn.run(make_app())
