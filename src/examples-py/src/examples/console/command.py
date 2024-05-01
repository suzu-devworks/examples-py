import importlib.metadata
from argparse import ArgumentParser, RawTextHelpFormatter
from logging import getLogger

from examples.libraries.argparse import configure_parser as configure_argparse_parser
from examples.libraries.logging import configure_logging
from examples.libraries.logging import configure_parser as configure_logging_parser

configure_logging()
logger = getLogger("examples.console.command")

__version__ = importlib.metadata.version("examples-py")


def __parse_arguments():
    parser = ArgumentParser(
        description="console examples for argparse.",
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "-c",
        "--config",
        action="store",
        help="config file path.\n(default: %(default)s)",
        dest="config_file_path",
        default="./examples_config.yaml",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        help="show verbose output, -vv -vvv is even more.",
        default=0,
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="show version and exit",
    )

    subparsers = parser.add_subparsers(
        title="sub commands",
        description="for examples commands",
        help="choose command",
        required=True,
    )

    # argparse
    args_parser = subparsers.add_parser(
        "argparse",
        help="argparse example",
        description="standard library/argparse example",
    )
    configure_argparse_parser(args_parser)

    # logging
    logging_parser = subparsers.add_parser(
        "logging",
        help="logging example",
        description="standard library/logging example",
    )
    configure_logging_parser(logging_parser)

    args = parser.parse_args()

    return args


def main():
    args = __parse_arguments()

    logger.info("===== start... ")

    try:
        args.exec(args)
    except Exception:
        logger.exception("Exiting due to an unhandled exception.")

    logger.info("===== end. ")


if __name__ == "__main__":
    main()
