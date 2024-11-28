from argparse import ArgumentParser

from .mqueue import configure_arguments as configure_mqueue


def configure_arguments(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(required=True)

    mqueue_parser = subparsers.add_parser("mqueue", help="POSIX IPC MessageQueue example")
    configure_mqueue(mqueue_parser)
