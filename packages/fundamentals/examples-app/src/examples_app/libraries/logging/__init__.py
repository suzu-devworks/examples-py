from argparse import ArgumentParser

from .configuration import configure_logging
from .example import do_example
from .filter import NoPasswordFilter, level_filter_factory


def configure_arguments(parser: ArgumentParser) -> None:
    parser.set_defaults(exec=lambda args: do_example(args))


__all__ = [
    "configure_logging",
    "configure_arguments",
    "level_filter_factory",
    "NoPasswordFilter",
]
