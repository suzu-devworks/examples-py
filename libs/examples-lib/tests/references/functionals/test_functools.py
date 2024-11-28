"""This test is for learning how to use the functools module used in iterators.

References:
    - https://docs.python.org/ja/3/howto/functional.html#the-functools-module
    - https://book.pythontips.com/en/latest/map_filter.html

"""

import operator
from functools import reduce


def test_using_functools_reduce() -> None:
    """`functools.reduce(function, iterable[, initializer])`

    Apply function of two arguments cumulatively to the items of iterable,
    from left to right, so as to reduce the iterable to a single value
    """

    list1 = ["A", "BB", "C"]
    actual1 = reduce(operator.concat, list1)  # type: ignore[arg-type]
    # spell-checker:disable-next-line
    assert actual1 == "ABBC"

    range1 = range(1, 11)
    actual2 = reduce(lambda x, y: x + y, range1)
    assert actual2 == 55
