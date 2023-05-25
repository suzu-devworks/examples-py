import sys
from argparse import ArgumentParser, FileType, Namespace
from enum import Enum
from io import TextIOWrapper
from logging import getLogger

logger = getLogger(__name__)


class Game(Enum):
    rock = 1
    paper = 2
    scissors = 3

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_string(s: str) -> "Game":
        try:
            return Game[s]
        except KeyError:
            raise ValueError()


def configure_parser(parser: ArgumentParser) -> None:
    parser.add_argument(
        "infiles",
        help="input file[s]",
        nargs="*",
        type=FileType("r"),
        default=sys.stdin,
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
        type=lambda s: Game.from_string(s),
        choices=list(Game),
        dest="param_choices",
        help="choices",
    )
    parser.set_defaults(exec=lambda args: do_argument_sample(args))


def do_argument_sample(args: Namespace) -> None:
    logger.info(args)

    inputs: list[TextIOWrapper] = args.infile
    output: TextIOWrapper = args.outfile

    try:
        for input in inputs:
            data = input.read()
            output.write(data)

            # argparse.FileType does not close.
            if input.name != "<stdin>":
                input.close()

    except KeyboardInterrupt:
        logger.warning("interrupt!")

    # argparse.FileType does not close.
    if output.name != "<stdout>":
        output.close()
