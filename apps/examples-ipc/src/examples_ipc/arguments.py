import importlib.metadata
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter

from .posix import configure_arguments as configure_posix
from .sysv import configure_arguments as configure_sysv

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

    posix_parser = subparsers.add_parser("posix", help="POSIX IPC examples")
    configure_posix(posix_parser)

    sysv_parser = subparsers.add_parser("sysv", help="SystemV IPC examples")
    configure_sysv(sysv_parser)

    args = parser.parse_args()
    return args
