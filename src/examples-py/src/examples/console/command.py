from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from logging import getLogger

from examples.libraries.logging import configure_logging

from .arguments import configure_arguments

configure_logging()
_logger = getLogger("examples.console.command")


def _parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="console examples for argparse.",
        formatter_class=RawTextHelpFormatter,
    )
    configure_arguments(parser)

    subparsers = parser.add_subparsers(
        title="sub commands",
        description="for examples commands",
        help="choose command",
        required=True,
    )

    # argparse
    from examples.libraries.argparse import configure_arguments as configure_args_argparse

    args_parser = subparsers.add_parser(
        "argparse",
        help="argparse example",
        description="standard library/argparse example",
    )
    configure_args_argparse(args_parser)

    # logging
    from examples.libraries.logging import configure_arguments as configure_args_logging

    logging_parser = subparsers.add_parser(
        "logging",
        help="logging example",
        description="standard library/logging example",
    )
    configure_args_logging(logging_parser)

    # spell-checker:words exif
    # pillow exif
    from examples.libraries.pillow.exif import configure_arguments as configure_args_exif

    exif_parser = subparsers.add_parser(
        "exif",
        help="exif example",
        description="pypi library/pillow example",
    )
    configure_args_exif(exif_parser)

    args = parser.parse_args()

    return args


def main() -> None:
    args = _parse_arguments()
    _logger.info("#start")

    try:
        args.exec(args)
    except Exception:
        _logger.exception("Exiting due to an unhandled exception.")

    _logger.info("#end")


if __name__ == "__main__":
    main()
