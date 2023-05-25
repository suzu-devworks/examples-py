# import importlib.metadata
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from logging import getLogger

from examples import __version__
from examples.config.logging import configure_logging

configure_logging()
logger = getLogger("examples.console.command")

# __version__ = importlib.metadata.version("examples-py")


def __parse_arguments() -> Namespace:
    from examples.console._argparse import configure_parser
    from examples.console._exif import configure_parser as configure_exif
    from examples.console._logging import do_logging_sample

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
    args_parser = subparsers.add_parser("args", help="argparse example", description="Lib/argparse example")
    configure_parser(args_parser)

    # logging
    logging_parser = subparsers.add_parser("logging", help="logging example", description="Lib/logging example")
    logging_parser.set_defaults(exec=lambda args: do_logging_sample(args))

    # exif
    exif_parser = subparsers.add_parser("exif", help="exif example", description="Lib/pillow example")
    configure_exif(exif_parser)

    args = parser.parse_args()

    return args


def main() -> None:
    args = __parse_arguments()

    logger.info("===== start... ")

    try:
        args.exec(args)
    except Exception:
        logger.exception("Exiting due to an unhandled exception.")

    logger.info("===== end. ")


if __name__ == "__main__":
    main()
