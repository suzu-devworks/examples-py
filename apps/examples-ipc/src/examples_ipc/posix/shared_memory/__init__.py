from argparse import ArgumentParser, Namespace

import posix_ipc

from .client import run as _client_run
from .server import run as _service_run


def _clean(name: str) -> None:
    posix_ipc.unlink_shared_memory(name)
    print(f"{name} is removed.")


def _run(args: Namespace) -> None:
    if args.clean:
        _clean(args.name)

    elif args.is_server_mode:
        _service_run(args.name)

    else:
        _client_run(args.name)


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
        "-n",
        "--name",
        dest="name",
        help="shared memory name.",
        default="/test-shm",
    )
    parser.set_defaults(exec=lambda args: _run(args))
