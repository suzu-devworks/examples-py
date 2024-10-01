"""This test is for learning sequence sorting.

References:
    - https://docs.python.org/ja/3/howto/sorting.html

"""

from operator import attrgetter, itemgetter, methodcaller


class TestSorting(object):
    def test_sort_or_sorted(self) -> None:
        """`sort` or `sorted`.

        - The `sort()` mutates the list without returning a return value. This is the same for the `reverse()`.
        - The `sort()` target a list, while the `sorted()` function target an iterator.
        """

        list1 = ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # sorted is stable sort.
        sorted_result = sorted(list1)
        assert sorted_result == [
            "Apple",
            "Banana",
            "Kiwi",
            "apple",
            "banana",
            "orange",
            "pear",
        ]
        assert list1 == ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # sort is unstable sort.
        sort_result = list1.sort()
        assert sort_result is None
        assert list1 == ["Apple", "Banana", "Kiwi", "apple", "banana", "orange", "pear"]

    def test_sorted_with_key(self) -> None:
        list1 = ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # ignore case sort.
        sorted_result = sorted(list1, key=lambda x: x.lower())
        assert sorted_result == [
            "Apple",
            "apple",
            "Banana",
            "banana",
            "Kiwi",
            "orange",
            "pear",
        ]

        # sort key slicing.
        sorted_result = sorted(list1, key=lambda x: x[1:])
        assert sorted_result == [
            "Banana",
            "banana",
            "pear",
            "Kiwi",
            "Apple",
            "apple",
            "orange",
        ]

    def test_sorted_with_operator(self) -> None:
        tuples = [
            ("john", "A", 15),
            ("jane", "B", 12),
            ("dave", "B", 10),
        ]

        # use operator.itemgetter
        sorted_by_itemgetter = sorted(tuples, key=itemgetter(2))
        assert [x[0] for x in sorted_by_itemgetter] == ["dave", "jane", "john"]

        class Student:
            def __init__(self, name: str, grade: str, age: int):
                self.name = name
                self.grade = grade
                self.age = age

            def get_age(self, reverse: bool) -> int:
                return self.age

        students = [
            Student("john", "A", age=15),
            Student("jane", "B", age=12),
            Student("dave", "B", age=10),
        ]

        sorted_by_age = sorted(students, key=lambda student: student.age)
        assert [x.name for x in sorted_by_age] == ["dave", "jane", "john"]

        # use operator.attrgetter
        sorted_by_attrgetter = sorted(students, key=attrgetter("age"))
        assert [x.name for x in sorted_by_attrgetter] == ["dave", "jane", "john"]

        # use operator.methodcaller
        sorted_by_methodcaller = sorted(students, key=methodcaller("get_age", {"reverse": False}))
        assert [x.name for x in sorted_by_methodcaller] == ["dave", "jane", "john"]

    def test_reversed_sorted(self) -> None:
        list1 = ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # Descending sort use reverse parameter.
        sorted_result = sorted(list1, reverse=True)
        assert isinstance(sorted_result, list)
        assert list(sorted_result) == [
            "pear",
            "orange",
            "banana",
            "apple",
            "Kiwi",
            "Banana",
            "Apple",
        ]

        # Descending sort use reversed.
        sorted_reversed_result = reversed(sorted(list1))
        assert not isinstance(sorted_reversed_result, list)
        assert list(sorted_reversed_result) == [
            "pear",
            "orange",
            "banana",
            "apple",
            "Kiwi",
            "Banana",
            "Apple",
        ]

        # reversed returns a reversed iteration while preserving the order of the elements.
        reserved_result = reversed(list1)
        assert list(reserved_result) == [
            "banana",
            "apple",
            "Kiwi",
            "Banana",
            "pear",
            "Apple",
            "orange",
        ]
