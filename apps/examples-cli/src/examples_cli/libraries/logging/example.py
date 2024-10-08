from argparse import Namespace
from logging import getLogger

logger = getLogger(__name__)


def do_example(args: Namespace) -> None:
    logger.info("-> logging example started: %s", args)

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
    # spell-checker:disable-next-line
    logger.info("----- p@ssword : xxxxxx, not filtering.")
