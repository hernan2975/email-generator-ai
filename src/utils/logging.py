
from loguru import logger
import sys

def configure_logging():
    logger.remove()
    logger.add(
        sys.stderr,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="INFO"
    )
    logger.add("logs/app.log", rotation="1 week")
