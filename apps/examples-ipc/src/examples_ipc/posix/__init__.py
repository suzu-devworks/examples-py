from argparse import ArgumentParser

from .mqueue import configure_arguments as configure_mqueue
from .shm import configure_arguments as configure_shm
from .semaphore import configure_arguments as configure_semaphore


def configure_arguments(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(required=True)

    mqueue_parser = subparsers.add_parser("mqueue", help="POSIX IPC MessageQueue example")
    configure_mqueue(mqueue_parser)

    shm_parser = subparsers.add_parser("shm", help="POSIX IPC SharedMemory example")
    configure_shm(shm_parser)

    semaphore_parser = subparsers.add_parser("semaphore", help="POSIX IPC Semaphore example")
    configure_semaphore(semaphore_parser)
