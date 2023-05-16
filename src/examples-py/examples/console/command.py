from logging import getLogger

from examples.config.logging import configure_logging
from examples.console.logging import do_logging_sample

configure_logging()


def main():
    logger = getLogger("examples.console.command")
    logger.info("start")

    try:
        do_logging_sample()
    except Exception:
        logger.exception("Exiting due to an unhandled exception.")

    logger.info("end")


if __name__ == "__main__":
    main()
