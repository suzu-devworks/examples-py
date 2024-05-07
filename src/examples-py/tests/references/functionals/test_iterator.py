"""This test is for learning the basic behavior of iterators.

References:
    - https://docs.python.org/ja/3/howto/functional.html#iterators

"""


class TestIterator:

    def test_iterator_basic(self) -> None:
        """`iter(object)`

        Return an iterator object.
        """
        list = [1, 2, 3]
        iterator = iter(list)
        assert iterator.__next__() == 1  # same as next(it)
        assert next(iterator) == 2
        assert next(iterator) == 3

        try:
            next(iterator)
            raise AssertionError("Unexpected results")
        except Exception as e:
            print("Expected!", e)
            pass

    def test_iterator_with_for_loop(self) -> None:
        list = [1, 2, 3]

        actual = []
        for i in iter(list):
            actual.append(i)

        assert actual == [1, 2, 3]

        actual = []
        for i in list:
            actual.append(i)

        assert actual == [1, 2, 3]

    def test_iterator_to_tuple(self) -> None:
        list = [1, 2, 3]

        iterator = iter(list)
        actual = tuple(iterator)

        assert actual != [1, 2, 3]  # type: ignore[comparison-overlap]
        assert actual == (1, 2, 3)

        # sequence unpack
        iterator = iter(list)
        a, b, c = iterator

        assert (a, b, c) == (1, 2, 3)

    pass
