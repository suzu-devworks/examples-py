import sys
from argparse import ArgumentParser, FileType

from .example import do_example
from .game import Game


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
    parser.set_defaults(exec=lambda args: do_example(args))
