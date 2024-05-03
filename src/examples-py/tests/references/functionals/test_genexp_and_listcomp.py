"""This test is for learning how to create iterators using generators.

References:
    - https://docs.python.org/ja/3/howto/functional.html#generator-expressions-and-list-comprehensions

"""


class TestGeneratorExpressionsAndListComprehensions:
    def test_remove_all_whitespace(self):
        """Remove all whitespace from a string stream."""

        line_list = ["  line 1\n", "line 2  \n", " \n", ""]

        # Generator expression -- returns iterator
        stripped_iter = (line.strip() for line in line_list)

        assert list(stripped_iter) == ["line 1", "line 2", "", ""]

        # List comprehension -- returns list
        stripped_list = [line.strip() for line in line_list if line != ""]

        assert stripped_list == ["line 1", "line 2", ""]
