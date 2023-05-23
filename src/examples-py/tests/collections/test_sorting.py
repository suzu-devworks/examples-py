"""
This test to learn sequence sorting.

References:
- https://docs.python.org/ja/3/howto/sorting.html
- https://github.com/SethMMorton/natsort

"""
import os
from operator import attrgetter, itemgetter, methodcaller

from natsort import natsorted, ns, os_sorted, realsorted


class TestSorting(object):
    def test_sort_or_sorted(self):
        """
        ### `sort` or `sorted`

        - The `sort()` mutates the list without returning a return value. This is the same for the `reverse()`.
        - The `sort()` target a list, while the `sorted()` function target an iterator.
        """

        list1 = ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # sorted is stable sort.
        sorted_result = sorted(list1)
        assert sorted_result == ["Apple", "Banana", "Kiwi", "apple", "banana", "orange", "pear"]
        assert list1 == ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # sort is unstable sort.
        sort_reault = list1.sort()
        assert sort_reault is None
        assert list1 == ["Apple", "Banana", "Kiwi", "apple", "banana", "orange", "pear"]

    def test_sorted_with_key(self):
        list1 = ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # ignore case sort.
        sorted_result = sorted(list1, key=lambda x: x.lower())
        assert sorted_result == ["Apple", "apple", "Banana", "banana", "Kiwi", "orange", "pear"]

        # sort key slicing.
        sorted_result = sorted(list1, key=lambda x: x[1:])
        assert sorted_result == ["Banana", "banana", "pear", "Kiwi", "Apple", "apple", "orange"]

    def test_sorted_with_operator(self):
        tuples = [
            ("john", "A", 15),
            ("jane", "B", 12),
            ("dave", "B", 10),
        ]

        # use operator.itemgetter
        sorted_by_itemgetter = sorted(tuples, key=itemgetter(2))
        assert [x[0] for x in sorted_by_itemgetter] == ["dave", "jane", "john"]

        class Student:
            def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age

            def get_age(self, reverse: bool):
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

    def test_reversed_sorted(self):
        list1 = ["orange", "Apple", "pear", "Banana", "Kiwi", "apple", "banana"]

        # Descending sort use reverse parameter.
        sorted_result = sorted(list1, reverse=True)
        assert isinstance(sorted_result, list)
        assert list(sorted_result) == ["pear", "orange", "banana", "apple", "Kiwi", "Banana", "Apple"]

        # Descending sort use reversed.
        sorted_result = reversed(sorted(list1))
        assert not isinstance(sorted_result, list)
        assert list(sorted_result) == ["pear", "orange", "banana", "apple", "Kiwi", "Banana", "Apple"]

        # reversed returns a reversed iteration while preserving the order of the elements.
        reserved_result = reversed(list1)
        assert list(reserved_result) == ["banana", "apple", "Kiwi", "Banana", "pear", "Apple", "orange"]

    def test_natural_sorting(self):
        list1 = ["2 ft 7 in", "1 ft 5 in", "10 ft 2 in", "2 ft 11 in", "7 ft 6 in"]

        # use normal sorted
        sorted_result = sorted(list1)
        assert sorted_result == ["1 ft 5 in", "10 ft 2 in", "2 ft 11 in", "2 ft 7 in", "7 ft 6 in"]

        # use natsorted
        natural_result = natsorted(list1)
        assert natural_result == ["1 ft 5 in", "2 ft 7 in", "2 ft 11 in", "7 ft 6 in", "10 ft 2 in"]

        # version number sort
        list2 = ["version-1.9", "version-2.0", "version-1.11", "version-1.10"]
        natural_result = natsorted(list2)
        assert natural_result == ["version-1.9", "version-1.10", "version-1.11", "version-2.0"]

    def test_natural_real_sorting(self):
        """
        Real(signed float valus) sorting.
        """

        #                +5.10                 -3.00             +5.30               +2.00
        list1 = ["position5.10.data", "position-3.data", "position5.3.data", "position2.data"]

        # use natsorted
        natural_result = natsorted(list1)
        assert natural_result == ["position2.data", "position5.3.data", "position5.10.data", "position-3.data"]

        # use natsorted with REAL parameter
        real_result = natsorted(list1, alg=ns.REAL)
        assert real_result == ["position-3.data", "position2.data", "position5.10.data", "position5.3.data"]

        # use realsorted, shortcut for natsorted with alg=ns.REAL
        real_result = realsorted(list1)
        assert real_result == ["position-3.data", "position2.data", "position5.10.data", "position5.3.data"]

    def test_natial_windows_sorting(self):
        """
        Return value that will be different depending on your platform.
        """

        dirs = os.listdir(".")
        _ = os_sorted(dirs)
        pass
