"""This test is for learning how to create iterators using generators.

References:
    - https://docs.python.org/ja/3/howto/functional.html#generators
    - https://docs.python.org/ja/3/reference/expressions.html?highlight=generator#generator-expressions

"""


class TestGenerator:
    def test_yield_generator(self):
        """The `yield` expression is
        used when defining a generator function or an asynchronous generator
        function and thus can only be used in the body of a function definition
        """

        def simple_generator():
            yield 1
            yield 2
            yield 3

        iterator = simple_generator()
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3

    def test_yield_from_generator(self):
        """`yield from <expr>` is
        given an iterable expression, and the value produced by iterating
        over the iterable expression is passed to the caller of the generator's method.
        """

        def simple_generator():
            yield from [1, 2]
            yield 3

        iterator = simple_generator()
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3

    def test_passing_values_into_a_generator(self):
        """(yield <expr>) or (yield from <expr>) is
        A simple way to pass values to a generator.
        """

        def counter(maximum):
            i = 0
            while i < maximum:
                # fmt: off
                val = (yield i)
                # fmt: on
                # If value provided, change counter
                if val is not None:
                    i = val
                else:
                    i += 1

        iterator = counter(10)
        assert next(iterator) == 0
        assert next(iterator) == 1
        assert iterator.send(8) == 8
        assert next(iterator) == 9

        try:
            next(iterator)
            raise Exception("Unexpected results")
        except Exception as e:
            print("Expected!", e)
            pass
