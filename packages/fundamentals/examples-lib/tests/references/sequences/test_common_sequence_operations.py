"""This test is for learning common operations on sequences.

References:
    - https://docs.python.org/ja/3/library/stdtypes.html#sequence-types-list-tuple-range
"""


def test_sequence_length() -> None:
    # fmt: off
    matrix = [
        [[1, 1], [1, 2], [1, 3]],
        [[2, 1], [2, 2], [2, 3]],
        [[3, 1], [3, 2], [3, 3]],
        [[4, 1], [4, 2], [4, 3]],
    ]
    # fmt: on

    assert len(matrix) == 4
    assert len(matrix[0]) == 3
    assert len(matrix[0][0]) == 2


def test_sequence_slice() -> None:
    """`sequence[start:stop:step]`

    [ 0, 1, 2, 3, 4, ... -4, -3, -2, -1 ]
    """
    alphabets = [chr(ord("a") + i) for i in range(0, 26)]
    strings = "".join(alphabets)

    assert alphabets[2:5] == ["c", "d", "e"]
    assert strings[2:5] == "cde"

    assert alphabets[20:] == ["u", "v", "w", "x", "y", "z"]
    # spell-checker:disable-next-line
    assert strings[20:] == "uvwxyz"

    assert alphabets[20:-1] == ["u", "v", "w", "x", "y"]
    # spell-checker:disable-next-line
    assert strings[20:-1] == "uvwxy"

    assert alphabets[:10] == ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    # spell-checker:disable-next-line
    assert strings[:10] == "abcdefghij"

    # start < end (positive)
    assert alphabets[0:3] == ["a", "b", "c"]
    assert alphabets[0:3:-1] == []
    # start > end (positive)
    assert alphabets[3:0] == []
    assert alphabets[3:0:-1] == ["d", "c", "b"]
    # start = end (positive)
    assert alphabets[3:3] == []

    # start < end (negative)
    assert alphabets[-4:-1] == ["w", "x", "y"]
    assert alphabets[-4:-1:-1] == []
    # start > end (negative)
    assert alphabets[-1:-4] == []
    assert alphabets[-1:-4:-1] == ["z", "y", "x"]
    # start = end (negative)
    assert alphabets[-4:-4] == []

    # ::step
    assert alphabets[::3] == ["a", "d", "g", "j", "m", "p", "s", "v", "y"]

    # ::step reversed
    # fmt: off
    assert alphabets[::-1] == ["z", "y", "x", "w", "v", "u", "t", "s", "r",
                                "q", "p", "o", "n", "m", "l", "k", "j", "i",
                                "h", "g", "f", "e", "d", "c", "b", "a"]
    # fmt: on
