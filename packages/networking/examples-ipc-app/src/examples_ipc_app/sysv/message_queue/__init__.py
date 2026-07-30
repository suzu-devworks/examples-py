from argparse import ArgumentParser, Namespace

import sysv_ipc

from .client import run as _client_run
from .server import run as _service_run


def _clean(key: int) -> None:
    mq = sysv_ipc.MessageQueue(key)
    sysv_ipc.remove_message_queue(mq.id)
    print(f"{key} [msqid: {mq.id}] is removed.")
    # spell-checker:words msqid


def _run(args: Namespace) -> None:
    if args.clean:
        _clean(args.key)

    elif args.is_server_mode:
        _service_run(args.key)

    else:
        _client_run(args.key, args.count)


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
        "-k",
        "--key",
        type=int,
        help="messaging queue key.",
        default=100,
    )
    parser.set_defaults(exec=lambda args: _run(args))
