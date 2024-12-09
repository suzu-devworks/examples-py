"""This test is to learn ndarray indexing operations."""

from typing import Any

import numpy as np
import numpy.typing as npt
import pytest

ndarray = npt.NDArray[Any]


@pytest.fixture(scope="module")
def matrix() -> ndarray:
    # fmt: off
    return np.array(
        [[  0,  1,  2,  3,  4],
         [  5,  6,  7,  8,  9],
         [ 10, 11, 12, 13, 14],
         [ 15, 16, 17, 18, 19],
         [ 20, 21, 22, 23, 24]])
    # fmt: on


def test_single_element_indexing(matrix: ndarray) -> None:
    """Single element indexing works exactly like that for other standard Python sequences."""

    # if one indexes a multidimensional array with fewer indices than dimensions, one gets a sub-dimensional array.
    assert np.all(matrix[1] == np.array([5, 6, 7, 8, 9]))
    assert np.all(matrix[-1] == np.array([20, 21, 22, 23, 24]))

    # It is not necessary to separate each dimension’s index into its own set of square brackets.
    assert np.all(matrix[2, 2] == 12)
    assert np.all(matrix[2, -2] == 13)

    assert np.all(matrix[2][2] == 12)
    assert np.all(matrix[2][-2] == 13)


def test_slicing_and_striding(matrix: ndarray) -> None:
    """Basic slicing extends Python’s basic concept of slicing to N dimensions."""

    # The basic slice syntax is `i:j:k`
    # fmt: off
    assert np.all(matrix[1:2] == np.array([5, 6, 7, 8, 9]))
    assert np.all(matrix[1:4] == np.array(
        [[ 5,  6,  7,  8,  9],
         [10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19]]))
    assert np.all(matrix[1:4:2] == np.array(
        [[ 5,  6,  7,  8,  9],
         [15, 16, 17, 18, 19]]))
    # fmt: on

    # Negative `i`` and `j`` are interpreted as `n + i`` and `n + j``.
    # fmt: off
    assert np.all(matrix[-4:2] == np.array(
        [[5, 6, 7, 8, 9]]))
    assert np.all(matrix[1:-1] == np.array(
        [[ 5,  6,  7,  8,  9],
         [10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19]]))
    # fmt: on

    # Negative k makes stepping go towards smaller indices.
    # fmt: off
    assert np.all(matrix[1:4:-2] == np.empty((0, 5)))
    assert np.all(matrix[4:1:-2] == np.array(
        [[20, 21, 22, 23, 24],
         [10, 11, 12, 13, 14]]))
    # fmt: on

    # fmt: off
    assert np.all(matrix[1:4:2, 3:5] == np.array(
        [[ 8,  9],
         [18, 19]]))
    # fmt: on

    # fmt: off
    assert np.all(matrix[::-1] == np.array(
        [[20, 21, 22, 23, 24],
         [15, 16, 17, 18, 19],
         [10, 11, 12, 13, 14],
         [ 5,  6,  7,  8,  9],
         [ 0,  1,  2,  3,  4]]))

    assert np.all(matrix[::-1, ::-1] == np.array(
        [[24, 23, 22, 21, 20],
         [19, 18, 17, 16, 15],
         [14, 13, 12, 11, 10],
         [ 9,  8,  7,  6,  5],
         [ 4,  3,  2,  1,  0]]))
    # fmt: on

    assert np.all(matrix[1, :] == np.array([5, 6, 7, 8, 9]))
    assert np.all(matrix[1, ...] == np.array([5, 6, 7, 8, 9]))
    assert np.all(matrix[:, 1] == np.array([1, 6, 11, 16, 21]))
    assert np.all(matrix[..., 1] == np.array([1, 6, 11, 16, 21]))


def test_assigning_values() -> None:
    """Assigning values to indexed arrays."""

    matrix = np.arange(25).reshape((5, 5))
    matrix[1:3] = 100

    # fmt: off
    assert np.all(matrix == np.array(
        [[  0,   1,   2,   3,   4],
         [100, 100, 100, 100, 100],
         [100, 100, 100, 100, 100],
         [ 15,  16,  17,  18,  19],
         [ 20,  21,  22,  23,  24]]))
    # fmt: on

    matrix = np.arange(25).reshape((5, 5))
    matrix[:, 2:4] = 200

    # fmt: off
    assert np.all(matrix == np.array(
        [[  0,   1, 200, 200,   4],
         [  5,   6, 200, 200,   9],
         [ 10,  11, 200, 200,  14],
         [ 15,  16, 200, 200,  19],
         [ 20,  21, 200, 200,  24]]))
    # fmt: on
