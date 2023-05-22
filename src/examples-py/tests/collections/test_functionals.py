"""
This test to learn functional approach.

References:
- https://book.pythontips.com/en/latest/map_filter.html
- https://docs.python.org/ja/3/howto/functional.html
- https://docs.python.org/ja/3/library/functools.html?highlight=functools

"""  # noqa E501
from functools import reduce


class TestFunctionals:
    def test_map(self):
        """
        map(function, iterable, *iterables)
        """
        list1 = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x**2, list1))
        assert squared == [1, 4, 9, 16, 25]

        list1 = range(1, 11)
        cubed = list(map(lambda x: x * x * x, range(1, 11)))
        assert cubed == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

    def test_filter(self):
        """
        filter(function, iterable)
        """
        list1 = range(2, 25)
        filterd = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, list1))
        assert filterd == [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

    def test_reduce(self):
        """
        reduce(function, iterable[, initializer])
        """
        list1 = range(1, 11)
        actual = reduce(lambda x, y: x + y, list1)
        assert actual == 55
