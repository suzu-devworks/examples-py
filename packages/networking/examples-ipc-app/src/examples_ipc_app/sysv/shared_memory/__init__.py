from argparse import ArgumentParser, Namespace

import sysv_ipc

from .client import run as _client_run
from .server import run as _service_run


def _clean(key: int) -> None:
    shm = sysv_ipc.SharedMemory(key)
    sysv_ipc.remove_shared_memory(shm.id)
    print(f"{key} [shmid: {shm.id}] is removed.")
    # spell-checker:words shmid


def _run(args: Namespace) -> None:
    if args.clean:
        _clean(args.key)

    elif args.is_server_mode:
        _service_run(args.key, args.size)

    else:
        _client_run(args.key, args.size)


def configure_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "--clean",
        action="store_true",
        help="clean message queue.",
    )
    parser.add_argument(
        "-s",
        "--server",
        action="store_true",
        dest="is_server_mode",
        help="run as a service and displays the contents of the shared memory.",
        default=False,
    )
    parser.add_argument(
        "-k",
        "--key",
        type=int,
        help="shared memory key.",
        default=100,
    )
    parser.add_argument(
        "-b",
        "--size",
        type=int,
        help="shared memory bytes size.",
        default=20,
    )
    parser.set_defaults(exec=lambda args: _run(args))
