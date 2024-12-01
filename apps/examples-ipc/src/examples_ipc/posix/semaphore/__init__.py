from argparse import ArgumentParser, Namespace

import posix_ipc

from .client import run as _client_run
from .server import run as _service_run


def _clean(name: str) -> None:
    posix_ipc.unlink_semaphore(name)
    print(f"{name} is removed.")


def _run(args: Namespace) -> None:
    if args.clean:
        _clean(args.name)

    elif args.is_server_mode:
        _service_run(args.name, args.count)

    else:
        _client_run(args.name, args.count, args.release)


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
        "-n",
        "--name",
        dest="name",
        help="semaphore name.",
        default="/test-semaphore",
    )
    parser.set_defaults(exec=lambda args: _run(args))
