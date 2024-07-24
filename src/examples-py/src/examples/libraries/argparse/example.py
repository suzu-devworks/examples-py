import sys
from argparse import ArgumentParser, FileType, Namespace
from io import TextIOWrapper
from logging import getLogger

from .game import Game

logger = getLogger(__name__)


def _do_example(args: Namespace) -> None:
    logger.info("-> argparse example started: %s", args)

    # spell-checker:words infiles
    inputs: list[TextIOWrapper] = args.infiles
    output: TextIOWrapper = args.outfile

    try:
        for input in inputs:
            for line in input:
                # line contains newline
                output.write(line)

            # argparse.FileType does not close.
            if input.name != "<stdin>":
                input.close()

    except KeyboardInterrupt:
        logger.warning("interrupt!")

    # argparse.FileType does not close.
    if output.name != "<stdout>":
        output.close()


def configure_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "infiles",
        help="input file[s]",
        nargs="*",
        type=FileType("r"),
        default=[sys.stdin],
    )
    parser.add_argument(
        "-o",
        "--out",
        dest="outfile",
        help="output file",
        nargs="?",
        type=FileType("w"),
        default=sys.stdout,
    )
    parser.add_argument(
        "-b",
        "--bool",
        action="store_true",
        dest="param_bool",
        help="option (action=store_true)",
        default=False,
    )
    parser.add_argument(
        "-a",
        "--append",
        action="append",
        dest="param_append",
        help="option (action=append)",
    )
    parser.add_argument(
        "-e",
        "--extend",
        action="extend",
        dest="param_extend",
        help="option (action=extend)",
        nargs="+",
        type=str,
    )
    parser.add_argument(
        "-c",
        "--choices",
        # choices=["rock", "paper", "scissors"],
        type=Game.from_string,
        choices=list(Game),
        dest="param_choices",
        help="choices",
    )
    parser.set_defaults(exec=lambda args: _do_example(args))
