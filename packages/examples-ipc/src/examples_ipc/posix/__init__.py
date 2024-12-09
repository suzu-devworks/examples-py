from argparse import ArgumentParser

from .message_queue import configure_arguments as configure_msq
from .semaphore import configure_arguments as configure_sem
from .shared_memory import configure_arguments as configure_shm


def configure_arguments(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(required=True)

    msq_parser = subparsers.add_parser("msq", help="POSIX IPC MessageQueue example")
    configure_msq(msq_parser)

    shm_parser = subparsers.add_parser("shm", help="POSIX IPC SharedMemory example")
    configure_shm(shm_parser)

    sem_parser = subparsers.add_parser("sem", help="POSIX IPC Semaphore example")
    configure_sem(sem_parser)
