from argparse import ArgumentParser
from logging import getLogger

logger = getLogger(__name__)


def do_logging_sample(args: ArgumentParser) -> None:
    # use loggers
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")

    try:
        raise NotImplementedError()
    except Exception:
        logger.exception("What is doing when exception happens.")

    logger.critical("critical message")

    logger.info("----- password : qwerty, filtered?")
    logger.info("----- p@asswod : xxxxxx, not filtering.")
