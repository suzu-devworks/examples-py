import sys
from argparse import ArgumentParser, FileType

from .example import do_example


def configure_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "infile",
        help="input file",
    )
    parser.add_argument(
        "-o",
        "--out",
        dest="out",
        help="output stream",
        nargs="?",
        type=FileType("w"),
        default=sys.stdout,
    )
    parser.set_defaults(exec=lambda args: do_example(args))
