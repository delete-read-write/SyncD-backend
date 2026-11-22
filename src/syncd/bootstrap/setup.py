import logging

from syncd.bootstrap.config.settings import LoggingSettings

logger = logging.getLogger(__name__)


def setup_logging(*, settings: LoggingSettings) -> None:
    logging.basicConfig(
        level=settings.level,
        format=settings.fmt,
        datefmt=settings.datefmt,
        force=True,
    )
    logger.info("logging is setup!")
