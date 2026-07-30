"""This test is for learning how to write list comprehensions.

The notation is very difficult to read and understand for non-Python programmers,
but if you are told that the speed is different, you will want to write it that way.
It seems that the cost of `append` is high even in the loop.

A list comprehension consists of the following parts:

- An Input Sequence.
- A Variable representing members of the input sequence.
- An Optional Predicate expression.
- An Output Expression producing elements of the output list from members of the Input Sequence that satisfy the predicate.

```
 [ {Output Expression} for {Variable} in {Input Sequence} if {Optional Predicate} ]
```

References:
    - https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    - https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html

"""  # noqa E501


def test_list_comprehension_basic() -> None:
    """The same as the following code:

    ```py
    squares = []
    for x in range(10):
        squares.append(x**2)
    ```
    """
    list1 = [x**2 for x in range(10)]
    assert list1 == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def test_list_comprehension_with_optional_predicate() -> None:
    """The same as the following code:

    ```py
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))
    ```
    """
    list1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert list1 == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


def test_list_comprehension_with_output_expression() -> None:
    """The same as the following code:

    ```py
    extension = []
    for i in range(10):
        if i % 2 == 0:
            extension.append(i)
        else:
            extension.append(str(i))
    ```
    """
    list1 = [i if i % 2 == 0 else str(i) for i in range(10)]
    assert list1 == [0, "1", 2, "3", 4, "5", 6, "7", 8, "9"]


def test_nested_list_comprehensions() -> None:
    # Given a 3x4 matrix:
    # fmt: off
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
    # fmt: on

    # transpose rows and columns
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    assert transposed == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    # use zip:
    zipped = [[x, y, z] for x, y, z in zip(*matrix, strict=False)]
    assert zipped == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    # to flatten
    flatten = [x for row in matrix for x in row]
    assert flatten == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def test_dictionary_creation_from_sequence() -> None:
    dict1 = {f"{x}^3": x**3 for x in range(10)}
    assert dict1 == {
        "0^3": 0,
        "1^3": 1,
        "2^3": 8,
        "3^3": 27,
        "4^3": 64,
        "5^3": 125,
        "6^3": 216,
        "7^3": 343,
        "8^3": 512,
        "9^3": 729,
    }


def test_dictionary_append() -> None:
    dict1: dict[str, int | str] = {"KEY1": 1, "KEY2": 2}

    # use update()
    dict1.update({"KEY3": 123})
    assert dict1 == {"KEY1": 1, "KEY2": 2, "KEY3": 123}

    # use operator |=
    dict1 |= {"KEY4": "key-4"}
    assert dict1 == {"KEY1": 1, "KEY2": 2, "KEY3": 123, "KEY4": "key-4"}

    # use operator **
    dict1 = {**dict1, "KEY5": True}
    assert dict1 == {
        "KEY1": 1,
        "KEY2": 2,
        "KEY3": 123,
        "KEY4": "key-4",
        "KEY5": True,
    }


def test_dictionary_merging() -> None:
    dict1: dict[str, int | str] = {"KEY1": 1, "KEY2": 2, "KEY3": 3, "KEY4": 4, "KEY5": 5}
    dict2: dict[str, int | str] = {"KEY2": "string1", "KEY4": "string2", "KEY6": "string3"}

    # use operator **
    merged = {**dict1, **dict2}
    assert merged == {
        "KEY1": 1,
        "KEY2": "string1",
        "KEY3": 3,
        "KEY4": "string2",
        "KEY5": 5,
        "KEY6": "string3",
    }

    # use update (mutable marge)
    dict1.update(dict2)
    assert dict1 == {
        "KEY1": 1,
        "KEY2": "string1",
        "KEY3": 3,
        "KEY4": "string2",
        "KEY5": 5,
        "KEY6": "string3",
    }


def test_dictionary_key_matching() -> None:
    dict1 = {"KEY1": 1, "KEY2": 2, "KEY3": 3, "KEY4": 4, "KEY5": 5}
    dict2 = {"KEY2": "string1", "KEY4": "string2", "KEY6": "string3"}

    # Create a dictionary with only dict2 values with matching keys, output all keys of dict1:
    dict3 = {key: dict2.get(key) for key in dict1}
    assert dict3 == {
        "KEY1": None,
        "KEY2": "string1",
        "KEY3": None,
        "KEY4": "string2",
        "KEY5": None,
    }

    # Creates a dictionary by updating dict1 with values from dict2 that have matching keys,
    #  and prints all keys in dict1:
    dict4 = {key: dict2.get(key, value) for key, value in dict1.items()}
    assert dict4 == {
        "KEY1": 1,
        "KEY2": "string1",
        "KEY3": 3,
        "KEY4": "string2",
        "KEY5": 5,
    }
