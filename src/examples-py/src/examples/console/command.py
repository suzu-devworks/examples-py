from logging import getLogger

from examples.libraries.logging import configure_logging, do_logging_example

configure_logging()


def main() -> None:
    logger = getLogger("examples.console.command")
    logger.info("start")

    try:
        do_logging_example()
    except Exception:
        logger.exception("Exiting due to an unhandled exception.")

    logger.info("end")


if __name__ == "__main__":
    main()
