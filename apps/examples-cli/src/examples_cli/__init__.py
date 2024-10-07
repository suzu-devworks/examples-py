from logging import getLogger

from .arguments import parse_arguments
from .libraries.logging.configuration import configure_logging

configure_logging()
_logger = getLogger(__name__)


def main() -> int:
    args = parse_arguments()
    _logger.info("#start")

    try:
        args.exec(args)

    except Exception:
        _logger.exception("Exiting due to an unhandled exception.")
        return 1

    _logger.info("#end")
    return 0
