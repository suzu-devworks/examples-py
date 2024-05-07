from logging import Filter, LogRecord
from typing import Callable


class NoPasswordFilter(Filter):
    """Filter that prevents password from being output to the log:
    https://docs.python.org/3/howto/logging-cookbook.html#configuring-filters-with-dictconfig
    """

    def __init__(self, name: str = "") -> None:
        super().__init__(name)

    def filter(self, record: LogRecord) -> bool:
        log_message = record.getMessage()
        return "password" not in log_message


def level_filter_factory(level: str) -> Callable[[LogRecord], bool]:
    """Custom handling of levels:
    https://docs.python.org/3/howto/logging-cookbook.html#custom-handling-of-levels
    """
    import logging as original

    level = getattr(original, level)

    def filter(record: LogRecord) -> bool:
        # spell-checker:words levelno
        return record.levelno <= int(level)

    return filter
