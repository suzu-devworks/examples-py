from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from logging import getLogger

from examples.libraries.logging import configure_logging
from examples.libraries.logging.example import do_logging_example

configure_logging()
logger = getLogger("examples.console.command")


def _parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="console examples for argparse.",
        formatter_class=RawTextHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        title="sub commands",
        description="for examples commands",
        help="choose command",
        required=True,
    )

    # logging
    logging_parser = subparsers.add_parser(
        "logging",
        help="logging example",
        description="standard library/logging example",
    )
    logging_parser.set_defaults(exec=lambda args: do_logging_example())

    args = parser.parse_args()

    return args


def main() -> None:
    args = _parse_arguments()
    logger.info("#start")

    try:
        args.exec(args)
    except Exception:
        logger.exception("Exiting due to an unhandled exception.")

    logger.info("#end")


if __name__ == "__main__":
    main()
