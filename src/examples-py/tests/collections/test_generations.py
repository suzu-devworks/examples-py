"""
This test to learn sequence generations.

References:
- https://docs.python.org/ja/3/reference/expressions.html?highlight=generator#generator-expressions

"""  # noqa E501


class TestGenerations:
    def test_yield_generator(self):
        def simple_generator():
            yield 1
            yield 2
            yield 3

        iterator = simple_generator()
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3

    def test_yield_from_generator(self):
        def simple_generator():
            yield from [1, 2]
            yield 3

        iterator = simple_generator()
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3
