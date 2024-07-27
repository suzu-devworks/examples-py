import importlib.metadata
from argparse import ArgumentParser

_version = importlib.metadata.version("examples-py")


def configure_arguments(parser: ArgumentParser) -> None:
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
