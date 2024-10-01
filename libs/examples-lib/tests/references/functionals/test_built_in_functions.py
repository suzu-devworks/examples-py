"""This test is for learning built-in functions commonly used with iterators.

References:
    - https://docs.python.org/ja/3/howto/functional.html#built-in-functions
    - https://book.pythontips.com/en/latest/map_filter.html

"""


class TestBuiltInFunctions:
    def test_map(self) -> None:
        """`map(function, iterable, *iterables)`

        Return an iterator that applies function to every item of iterable,
        yielding the results.
        """
        list1 = [1, 2, 3, 4, 5]
        squared = list(map(lambda x: x**2, list1))
        assert squared == [1, 4, 9, 16, 25]

        # The same effect can be achieved using a list comprehension.
        squared_comp = [x**2 for x in list1]
        assert squared_comp == [1, 4, 9, 16, 25]

        list2 = range(1, 11)
        cubed = list(map(lambda x: x * x * x, list2))
        assert cubed == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

        # The same effect can be achieved using a list comprehension.
        cubed_comp = [x * x * x for x in list2]
        assert cubed_comp == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

    def test_filter(self) -> None:
        """`filter(function, iterable)`

        Construct an iterator from those elements of iterable
        for which function is true.
        """
        list1 = range(2, 25)
        filtered = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, list1))
        assert filtered == [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

        # The same effect can be achieved using a list comprehension.
        filtered_comp = [x for x in list1 if x % 3 == 0 or x % 5 == 0]
        assert filtered_comp == [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

    def test_enumerate(self) -> None:
        """`enumerate(iterable, start=0)`

        Return an enumerate object.
        """
        actual = []
        for item in enumerate(["subject", "verb", "object"]):
            actual.append(item)

        assert actual == [(0, "subject"), (1, "verb"), (2, "object")]

    def test_sorted(self) -> None:
        """`sorted(iterable, /, *, key=None, reverse=False)`

        Return a new sorted list from the items in iterable.
        """
        origin = [769, 7953, 9828, 6431, 8442, 9878, 6213, 2207]

        sorted_list = sorted(origin)
        assert sorted_list == [769, 2207, 6213, 6431, 7953, 8442, 9828, 9878]

        reversed_list = sorted(origin, reverse=True)
        assert reversed_list == [9878, 9828, 8442, 7953, 6431, 6213, 2207, 769]

        pure_reversed = reversed(origin)
        assert list(pure_reversed) == [
            2207,
            6213,
            9878,
            8442,
            6431,
            9828,
            7953,
            769,
        ]

    def test_any(self) -> None:
        """`any(iterable)`

        Return True if any element of the iterable is true.
        """
        assert any([0, 1, 0]) is True
        assert any([0, 0, 0]) is False
        assert any([1, 1, 1]) is True

        assert any([False, False, True]) is True
        assert any(["", "", "_"]) is True

    def test_all(self) -> None:
        """`all(iterable)`

        Return True if all elements of the iterable are true
        (or if the iterable is empty).
        """
        assert all([0, 1, 0]) is False
        assert all([0, 0, 0]) is False
        assert all([1, 1, 1]) is True

        assert all([True, True, True]) is True
        assert all(["a", "b", "c"]) is True

    def test_zip(self) -> None:
        """`zip(*iterables, strict=False)`

        Iterate over several iterables in parallel,
        producing tuples with an item from each one.
        """
        list1 = ["a", "b", "c"]
        second = (1, 2, 3)

        zipped = zip(list1, second)
        assert list(zipped) == [("a", 1), ("b", 2), ("c", 3)]

        list2 = ["d", "e"]
        zipped = zip(list2, second)
        # second: 3 is lost.
        assert list(zipped) == [("d", 1), ("e", 2)]
