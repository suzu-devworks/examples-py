import importlib.metadata
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter

_version = importlib.metadata.version("examples-cli")


def _configure_arguments(parser: ArgumentParser) -> None:
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
        version=f"%(prog)s {_version}",
        help="show version and exit",
    )


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="console examples for argparse.",
        formatter_class=RawTextHelpFormatter,
    )
    _configure_arguments(parser)

    subparsers = parser.add_subparsers(
        title="sub commands",
        description="for examples commands",
        help="choose command",
        required=True,
    )

    # argparse
    from .libraries.argparse import configure_arguments as configure_args_argparse

    args_parser = subparsers.add_parser(
        "argparse",
        help="argparse example",
        description="standard library/argparse example",
    )
    configure_args_argparse(args_parser)

    # logging
    from .libraries.logging import configure_arguments as configure_args_logging

    logging_parser = subparsers.add_parser(
        "logging",
        help="logging example",
        description="standard library/logging example",
    )
    configure_args_logging(logging_parser)

    # exif - pillow
    from .libraries.pillow.exif import configure_arguments as configure_args_exif

    exif_parser = subparsers.add_parser(
        "exif",
        help="exif example",
        description="pypi library/pillow example",
    )
    configure_args_exif(exif_parser)

    args = parser.parse_args()

    return args
