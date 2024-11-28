from argparse import ArgumentParser, Namespace

import posix_ipc

from .client import run as _client_run
from .server import run as _service_run


def _clean(queue_name: str) -> None:
    posix_ipc.unlink_message_queue(queue_name)
    print(f"{queue_name} is removed.")


def _run(args: Namespace) -> None:
    if args.clean:
        _clean(args.queue_name)

    elif args.is_server_mode:
        _service_run(args.queue_name)

    else:
        _client_run(args.queue_name, args.count)


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
        help="run as a service and displays the contents of the message queue.",
        default=False,
    )
    parser.add_argument(
        "-c",
        "--count",
        dest="count",
        type=int,
        help="the number of send in client mode.",
        default=10,
    )
    parser.add_argument(
        "-n",
        "--name",
        dest="queue_name",
        help="messaging queue name.",
        default="/test-queue",
    )
    parser.set_defaults(exec=lambda args: _run(args))
