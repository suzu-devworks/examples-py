import importlib.metadata
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter

from .posix import configure_arguments as configure_args_posix

_version = importlib.metadata.version("examples-ipc")


def _configure_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {_version}",
        help="show version and exit",
    )


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="messaging using posix ipc.",
        formatter_class=RawTextHelpFormatter,
    )
    _configure_arguments(parser)

    subparsers = parser.add_subparsers(required=True)

    args_parser = subparsers.add_parser("posix", help="POSIX IPC examples")
    configure_args_posix(args_parser)

    args = parser.parse_args()
    return args
