"""This test is for learning how to use the functools module used in iterators.

References:
    - https://docs.python.org/ja/3/howto/functional.html#the-functools-module
    - https://book.pythontips.com/en/latest/map_filter.html

"""

import operator
from functools import reduce


class TestFunctools:

    def test_reduce(self):
        """`functools.reduce(function, iterable[, initializer])`

        Apply function of two arguments cumulatively to the items of iterable,
        from left to right, so as to reduce the iterable to a single value
        """

        list1 = ["A", "BB", "C"]
        actual = reduce(operator.concat, list1)
        # spell-checker:disable-next-line
        assert actual == "ABBC"

        list1 = range(1, 11)
        actual = reduce(lambda x, y: x + y, list1)
        assert actual == 55
