from argparse import ArgumentParser, Namespace

import sysv_ipc

from .client import run as _client_run
from .server import run as _service_run


def _clean(key: int) -> None:
    sem = sysv_ipc.Semaphore(key)
    sysv_ipc.remove_semaphore(sem.id)
    print(f"{key} [semid: {sem.id}] is removed.")
    # spell-checker:words semid


def _run(args: Namespace) -> None:
    if args.clean:
        _clean(args.key)

    elif args.is_server_mode:
        _service_run(args.key, args.count)

    else:
        _client_run(args.key, args.count, args.release)


def configure_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "--clean",
        action="store_true",
        help="clean semaphore.",
    )
    parser.add_argument(
        "-s",
        "--server",
        action="store_true",
        dest="is_server_mode",
        help="run as a service and displays the contents of the semaphore.",
        default=False,
    )
    parser.add_argument(
        "-r",
        "--release",
        action="store_true",
        help="unset semaphore.",
    )
    parser.add_argument(
        "-c",
        "--count",
        dest="count",
        type=int,
        help="the initial semaphore value.",
        default=2,
    )
    parser.add_argument(
        "-k",
        "--key",
        type=int,
        help="semaphore key.",
        default=100,
    )
    parser.set_defaults(exec=lambda args: _run(args))
