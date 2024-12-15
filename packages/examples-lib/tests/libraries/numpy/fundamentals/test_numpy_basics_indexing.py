"""This test is for learning to Indexing on ndarrays from NumPy fundamentals section of the NumPy User Guide.

References:
    - https://numpy.org/doc/stable/user/basics.indexing.html
"""

from typing import Any

import numpy as np
import numpy.typing as npt
import pytest

ndarray = npt.NDArray[Any]


def test_single_element_indexing() -> None:
    """Single element indexing - Basic indexing,"""
    x = np.arange(10)

    # It is 0-based, and accepts negative indices for indexing from the end of the array.
    assert x[2] == 2
    assert x[-2] == 8

    x = x.reshape(2, 5)

    # It is not necessary to separate each dimension’s index into its own set of square brackets.
    assert x[1, 3] == 8
    assert x[1, -1] == 9

    # if one indexes a multidimensional array with fewer indices than dimensions,
    # one gets a sub-dimensional array.
    assert np.all(x[0] == np.array([0, 1, 2, 3, 4]))

    # In this case on the right side.
    # This is more inefficient because a new temporary array is created
    # with an initial index of 0 and then indexed by 2.
    assert x[0, 2] == x[0][2]


def test_slicing_and_striding() -> None:
    """Slicing and striding - Basic indexing."""

    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # The basic slice syntax is `i:j:k` where i is the starting index,
    # j is the stopping index, and k is the step (k != 0)
    assert np.all(x[1:7:2] == np.array([1, 3, 5]))

    # Negative i and j are interpreted as n + i and n + j
    # where n is the number of elements in the corresponding dimension.
    # Negative k makes stepping go towards smaller indices.
    assert np.all(x[-2:10] == np.array([8, 9]))
    assert np.all(x[-3:3:-1] == np.array([7, 6, 5, 4]))

    # Assume n is the number of elements in the dimension being sliced.
    # If i is not given it defaults to 0 for k > 0 and n - 1 for k < 0.
    # If j is not given it defaults to n for k > 0 and -n-1 for k < 0.
    # If k is not given it defaults to 1.
    # Note that `::` is the same as `:` and means select all indices along this axis.
    assert np.all(x[5:] == np.array([5, 6, 7, 8, 9]))
    assert np.all(x[:5] == np.array([0, 1, 2, 3, 4]))
    assert np.all(x[::5] == np.array([0, 5]))

    x = np.array([[[1], [2], [3]], [[4], [5], [6]]])
    assert x.shape == (2, 3, 1)

    # If the number of objects in the selection tuple is less than N,
    # then `:` is assumed for any subsequent dimensions.
    assert np.all(x[1:2] == np.array([[[4], [5], [6]]]))
    assert np.all(x[1:2, :, :] == np.array([[[4], [5], [6]]]))

    # An integer, i, returns the same values as `i:i+1` except the dimensionality of the returned object is reduced by 1.
    # In particular, a selection tuple with the p-th element an integer (and all other entries `:`)
    # returns the corresponding sub-array with dimension N - 1.
    assert np.all(x[1] == np.array([[4], [5], [6]]))
    assert np.all(x[1 : 1 + 1] == np.array([[[[4], [5], [6]]]]))
    assert x[0].shape == (3, 1)
    assert x[:, 0].shape == (2, 1)
    assert x[:, :, 0].shape == (2, 3)

    # If the selection tuple has all entries `:` except the p-th entry which is a slice object `i:j:k`,
    # then the returned array has dimension N formed by stacking, along the p-th axis,
    # the sub-arrays returned by integer indexing of elements i, i+k, …, i + (m - 1) k < j.
    assert np.all(x[1:2] == np.array([[[[4], [5], [6]]]]))
    assert np.all(x[:, 1:2] == np.array([[[2]], [[5]]]))
    assert np.all(x[:, :, 0:1] == np.array([[[1], [2], [3]], [[4], [5], [6]]]))
    assert x[1:2].shape == (1, 3, 1)
    assert x[:, 1:2].shape == (2, 1, 1)
    assert x[:, :, 0:1].shape == (2, 3, 1)

    # Basic slicing with more than one non-`:` entry in the slicing tuple,
    # acts like repeated application of slicing using a single non-`:` entry,
    # where the non-`:` entries are successively taken (with all other non-`:` entries replaced by `:`).
    # Thus, `x[ind1, ..., ind2,:]` acts like `x[ind1][..., ind2, :]` under basic slicing.
    assert np.all(x[0, 0, :] == np.array([1]))
    assert np.all(x[0][..., 0, :] == np.array([1]))
    assert np.all(x[:, 0, 0] == np.array([1, 4]))
    assert np.all(x[:][..., 0, 0] == np.array([1, 4]))
    assert np.all(x[0, :, 0] == np.array([[1, 2, 3]]))
    assert np.all(x[0][..., :, 0] == np.array([[1, 2, 3]]))

    # You may use slicing to set values in the array, but (unlike lists) you can never grow the array.
    # The size of the value to be set in `x[obj] = value` must be (broadcastable to) the same shape as `x[obj]`.
    # spell-checker:words broadcastable

    x = np.array([[[1], [2], [3]], [[4], [5], [6]]])
    assert x.shape == (2, 3, 1)

    with pytest.raises(ValueError) as e:
        x[0, :] = np.array([[2, 4], [6, 8]])
    assert "could not broadcast input array from shape" in str(e.value)

    x[0, :] = np.array([[2], [4], [6]])
    assert np.all(x == np.array([[[2], [4], [6]], [[4], [5], [6]]]))
    assert x.shape == (2, 3, 1)

    # A slicing tuple can always be constructed as obj and used in the x[obj] notation.
    # Slice objects can be used in the construction in place of the [start:stop:step] notation.
    # For example, x[1:10:5, ::-1] can also be implemented as obj = (slice(1, 10, 5), slice(None, None, -1)); x[obj]
    x = np.array([[[1], [2], [3]], [[4], [5], [6]]])

    assert np.all(x[1:10:5, ::-1] == np.array([[[6], [5], [4]]]))
    obj = (slice(1, 10, 5), slice(None, None, -1))
    assert np.all(x[obj] == np.array([[[6], [5], [4]]]))


def test_dimensional_indexing() -> None:
    """Dimensional indexing tools - Basic indexing."""

    x = np.array([[[1], [2], [3]], [[4], [5], [6]]])

    # Ellipsis expands to the number of : objects needed for the selection tuple to index all dimensions.
    assert np.all(x[..., 0] == np.array([[1, 2, 3], [4, 5, 6]]))
    assert np.all(x[:, :, 0] == np.array([[1, 2, 3], [4, 5, 6]]))

    # Each newaxis object in the selection tuple serves to expand the dimensions
    # of the resulting selection by one unit-length dimension.
    # newaxis is an alias for None
    assert np.all(x[:, np.newaxis, :, :] == np.array([[[[1], [2], [3]]], [[[4], [5], [6]]]]))
    assert x[:, np.newaxis, :, :].shape == (2, 1, 3, 1)
    assert x[:, None, :, :].shape == (2, 1, 3, 1)
    # spell-checker:words newaxis

    # For example:
    x = np.arange(5)
    actual = x[:, np.newaxis] + x[np.newaxis, :]

    # fmt: off
    assert np.all(actual == np.array(
        [[0, 1, 2, 3, 4],
         [1, 2, 3, 4, 5],
         [2, 3, 4, 5, 6],
         [3, 4, 5, 6, 7],
         [4, 5, 6, 7, 8]])
    )
    # fmt: on


def test_integer_array_indexing() -> None:
    """Integer array indexing - Advanced indexing."""

    # Integer array indexing allows selection of arbitrary items in the array based on their N-dimensional index.
    x = np.arange(10, 1, -1)

    assert np.all(x[np.array([3, 3, 1, 8])] == np.array([7, 7, 9, 2]))
    assert np.all(x[np.array([3, 3, -3, 8])] == np.array([7, 7, 4, 2]))

    #  the index values are out of bounds then an IndexError is thrown:
    x = np.array([[1, 2], [3, 4], [5, 6]])

    assert np.all(x[np.array([1, -1])] == np.array([[3, 4], [5, 6]]))
    with pytest.raises(IndexError) as e:
        x[np.array([3, 4])]
    assert "index 3 is out of bounds for axis 0 with size 3" in str(e.value)

    # The shape of the result is identical to the shape of the (broadcast) index array ind_1, ..., ind_N.
    x = np.arange(9).reshape(3, 3)

    assert np.array([2]).shape == (1,)
    assert x[np.array([2])].shape == (1, 3)

    assert np.array([2, 0]).shape == (2,)
    assert x[np.array([2, 0])].shape == (2, 3)

    assert np.array([[2]]).shape == (1, 1)
    assert x[np.array([[2]])].shape == (1, 1, 3)

    assert np.array([[2, 0]]).shape == (1, 2)
    assert x[np.array([[2, 0]])].shape == (1, 2, 3)

    # fmt: off
    y = np.array(
        [[ 0,  1,  2,  3,  4,  5,  6],
         [ 7,  8,  9, 10, 11, 12, 13],
         [14, 15, 16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25, 26, 27],
         [28, 29, 30, 31, 32, 33, 34]])
    # fmt: on

    # If the shapes of the index arrays are the same:
    assert np.all(y[np.array([0, 2, 4]), np.array([0, 1, 2])] == np.array([0, 15, 30]))
    assert np.all(np.array([y[0, 0], y[2, 1], y[4, 2]]) == np.array([0, 15, 30]))

    # If the index arrays do not have the same shape:
    with pytest.raises(IndexError) as e:
        y[np.array([0, 2, 4]), np.array([0, 1])]
    assert "shape mismatch: indexing arrays could not be broadcast" in str(e.value)

    # The broadcasting mechanism permits index arrays to be combined with scalars for other indices.
    assert np.all(y[np.array([0, 2, 4]), 1] == np.array([1, 15, 29]))

    # Indexed arrays allow you to only partially index an array.
    # fmt: off
    assert np.all(y[np.array([0, 2, 4])] == np.array(
        [[ 0,  1,  2,  3,  4,  5,  6],
         [14, 15, 16, 17, 18, 19, 20],
         [28, 29, 30, 31, 32, 33, 34]]))
    # fmt: on


def test_integer_array_indexing_examples() -> None:
    """Example: Integer array indexing - Advanced indexing.

    From a 4x3 array the corner elements should be selected using advanced indexing.
    """
    # fmt: off
    x = np.array(
        [[ 0,  1,  2],
         [ 3,  4,  5],
         [ 6,  7,  8],
         [ 9, 10, 11]])
    # fmt: on

    rows = np.array([[0, 0], [3, 3]], dtype=np.intp)
    columns = np.array([[0, 2], [0, 2]], dtype=np.intp)
    assert np.all(x[rows, columns] == np.array([[0, 2], [9, 11]]))
    # spell-checker:words intp

    # Use broadcasting.
    rows = np.array([0, 3], dtype=np.intp)
    columns = np.array([0, 2], dtype=np.intp)
    assert np.all(x[rows[:, np.newaxis], columns] == np.array([[0, 2], [9, 11]]))

    # Use `np.ix_`
    assert np.all(x[np.ix_(rows, columns)] == np.array([[0, 2], [9, 11]]))

    # Without the np.ix_ calls, only the diagonal elements are selected.
    assert np.all(x[rows, columns] == np.array([0, 11]))


def test_boolean_array_indexing() -> None:
    """Boolean array indexing - Advanced indexing."""
    # When filtering the values ​​of required elements
    x = np.array([[1.0, 2.0], [np.nan, 3.0], [np.nan, np.nan]])
    assert np.all(x[~np.isnan(x)] == np.array([1.0, 2.0, 3.0]))

    # When adding a constant to all negative elements
    x = np.array([1.0, -1.0, -2.0, 3])
    x[x < 0] += 20
    assert np.all(x == np.array([1.0, 19.0, 18.0, 3.0]))

    # When the number of dimensions of a Boolean array is less than
    # the number of dimensions of the array being indexed.
    x = np.arange(35).reshape(5, 7)
    b = x > 20
    assert np.all(b[:, 5] == np.array([False, False, False, True, True]))
    # fmt: off
    assert np.all(x[b[:, 5]] == np.array(
        [[21, 22, 23, 24, 25, 26, 27],
         [28, 29, 30, 31, 32, 33, 34]]))
    # fmt: on


def test_boolean_array_indexing_example1() -> None:
    """Example: Boolean array indexing - Advanced indexing.

    From an array, select all rows which sum up to less or equal two:
    """
    x = np.array([[0, 1], [1, 1], [2, 2]])
    rowsum = x.sum(axis=-1)
    # fmt: off
    assert np.all(x[rowsum <= 2, :] == np.array(
        [[0, 1],
         [1, 1]]))
    # fmt: on
    # spell-checker:words rowsum

    colsum = x.sum(axis=0)
    # fmt: off
    assert np.all(x[:, colsum <= 3] == np.array(
        [[0],
         [1],
         [2]]))
    # fmt: on
    # spell-checker:words colsum


def test_boolean_array_indexing_example2() -> None:
    """Example: Boolean array indexing - Advanced indexing.

    Use boolean indexing to select all rows adding up to an even number:
    """
    # fmt: off
    x = np.array(
        [[0,  1,  2],
         [3,  4,  5],
         [6,  7,  8],
         [9, 10, 11]])
    # fmt: on
    rows = (x.sum(-1) % 2) == 0
    columns = [0, 2]

    assert np.all(rows == np.array([False, True, False, True]))
    # fmt: off
    assert np.all(x[np.ix_(rows, columns)] == np.array(
        [[3, 5],
         [9, 11]]))
    # fmt: on


def test_boolean_array_indexing_example3() -> None:
    """Example: Boolean array indexing - Advanced indexing.

    Use a 2-D boolean array of shape (2, 3) with four True elements
    to select rows from a 3-D array of shape (2, 3, 5)
    results in a 2-D result of shape (4, 5):
    """
    # fmt: off
    x = np.array(
        [[[ 0,  1,  2,  3,  4],
          [ 5,  6,  7,  8,  9],
          [10, 11, 12, 13, 14]],
         [[15, 16, 17, 18, 19],
          [20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29]]])
    # fmt: on

    # fmt: off
    b = np.array(
        [[True, True, False],
         [False, True, True]])
    assert np.all(x[b] == np.array(
        [[ 0,  1,  2,  3,  4],
         [ 5,  6,  7,  8,  9],
         [20, 21, 22, 23, 24],
         [25, 26, 27, 28, 29]]))
    # fmt: on

    # fmt: off
    b = np.array(
        [[True, False, True],
         [False, False, True]])
    assert np.all(x[b] == np.array(
        [[ 0,  1,  2,  3,  4],
         [10, 11, 12, 13, 14],
         [25, 26, 27, 28, 29]]))
    # fmt: on


def test_combining_indexing() -> None:
    """Combining advanced and basic indexing - Advanced indexing."""
    y = np.arange(35).reshape(5, 7)

    # When to use only one advanced index in combination with slicing
    # fmt: off
    assert np.all(y[np.array([0, 2, 4]), 1:3] == np.array(
        [[ 1,  2],
         [15, 16],
         [29, 30]]))
    # fmt: on

    # This is equivalent to:
    # fmt: off
    assert np.all(y[:, 1:3][np.array([0, 2, 4]), :] == np.array(
        [[ 1,  2],
         [15, 16],
         [29, 30]]))
    # fmt: on

    # A slice is preferable when it is possible.
    x = np.arange(12).reshape(4, 3)
    assert np.all(x[1:2, 1:3] == np.array([[4, 5]]))
    assert np.all(x[1:2, [1, 2]] == np.array([[4, 5]]))

    # Example
    b = y > 20
    assert np.all(b[:, 5] == np.array([False, False, False, True, True]))
    # fmt: on
    assert np.all(y[b[:, 5], 1:3] == np.array([[22, 23], [29, 30]]))


def test_field_access() -> None:
    """Field access."""
    x = np.zeros((2, 2), dtype=[("a", np.int32), ("b", np.float64, (3, 3))])

    assert x["a"].shape == (2, 2)
    assert x["a"].dtype == np.int32
    assert x["b"].shape == (2, 2, 3, 3)  # type: ignore
    assert x["b"].dtype == np.float64


def test_flat_iterator_indexing() -> None:
    """Flat iterator indexing."""
    x = np.arange(12).reshape(4, 3)

    assert np.all(x[1] == np.array([3, 4, 5]))
    assert x.flat[1] == 1
    assert type(x.flat) is np.flatiter
    # spell-checker:words flatiter


def test_assigning_values() -> None:
    """Assigning values to indexed arrays."""

    # When assigning a constant to a slice:
    x = np.zeros(10, int)
    x[2:7] = 1
    assert np.all(x == np.array([0, 0, 1, 1, 1, 1, 1, 0, 0, 0]))

    # or an array of the right size:
    x = np.zeros(10, int)
    x[2:7] = np.arange(5)
    assert np.all(x == np.array([0, 0, 0, 1, 2, 3, 4, 0, 0, 0]))

    # When assigning float to int:
    x = np.zeros(10, int)
    x[1] = 1.2
    assert np.all(x == np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0]))

    # When assigning complex to floats or ints:
    x = np.zeros(10, int)
    with pytest.raises(TypeError) as e:
        x[1] = 1.2j
    assert "int() argument must be a string, a bytes-like object or a real number, not 'complex'" in str(e.value)

    # Some actions may simply not work as expected:
    x = np.arange(0, 50, 10)
    assert np.all(x == np.array([0, 10, 20, 30, 40]))
    x[np.array([1, 1, 3, 1])] += 1
    # `[1] != 13` The array value of `x[1] + 1` is assigned to `x[1]` three times.
    assert np.all(x == np.array([0, 11, 20, 31, 40]))


def test_variable_numbers_of_indices() -> None:
    """Dealing with variable numbers of indices within programs."""

    # If one supplies to the index a tuple, the tuple will be interpreted as a list of indices:
    z = np.arange(81).reshape(3, 3, 3, 3)

    indices = (1, 1, 1, 1)
    assert z[indices] == 40

    indices = (1, 1, 1, slice(0, 2))  # same as [1, 1, 1, 0:2]
    assert np.all(z[indices] == np.array([39, 40]))

    indices = (1, Ellipsis, 1)  # same as [1, ..., 1]
    assert np.all(z[indices] == np.array([[28, 31, 34], [37, 40, 43], [46, 49, 52]]))
