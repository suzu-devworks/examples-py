from argparse import ArgumentParser

from .message_queue import configure_arguments as configure_msg
from .semaphore import configure_arguments as configure_sem
from .shared_memory import configure_arguments as configure_shm


def configure_arguments(parser: ArgumentParser) -> None:
    subparsers = parser.add_subparsers(required=True)

    msg_parser = subparsers.add_parser("msq", help="SystemV IPC MessageQueue example")
    configure_msg(msg_parser)

    shm_parser = subparsers.add_parser("shm", help="SystemV IPC SharedMemory example")
    configure_shm(shm_parser)

    sem_parser = subparsers.add_parser("sem", help="SystemV IPC Semaphore example")
    configure_sem(sem_parser)
