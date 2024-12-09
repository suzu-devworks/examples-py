"""This test is for learning ndarray broadcasting operations."""

import numpy as np
import pytest


def test_broadcast_same_shape() -> None:
    """When the two arrays have exactly the same shape."""

    # 1D arrays
    A = np.array([1.0, 2.0, 3.0])
    B = np.array([2.0, 2.0, 2.0])

    actual = A * B

    # A * B = [(a1 * b1), (a2 * b2), (a3 * b3)]
    expected = np.array([2.0, 4.0, 6.0])
    assert np.all(actual == expected)

    # 2D arrays
    # fmt: off
    A = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    B = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    # fmt: on

    actual = A * B

    # A * B = [[(a11 * b11), (a12 * b12), (a13 * b13)]
    #          [(a21 * b21), (a22 * b22), (a23 * b23)]
    #          [(a31 * b31), (a32 * b32), (a33 * b33)]]
    # fmt: off
    expected = np.array([[ 0,  1,  4],
                         [ 9, 16, 25],
                         [36, 49, 64]])
    # fmt: on
    assert np.all(actual == expected)


def test_broadcast_by_scalar() -> None:
    """when an array and a scalar value are combined in an operation."""

    A = np.array([1.0, 2.0, 3.0])
    k = 2

    actual = A * k

    # A * k = [(a1 * k), (a2 * k), (a3 * k)]
    expected = np.array([2.0, 4.0, 6.0])
    assert np.all(actual == expected)

    # fmt: off
    A = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    k = 3
    # fmt: on

    actual = A * k

    # A * k = [[(a11 * k), (a12 * k), (a13 * k)]
    #          [(a21 * k), (a22 * k), (a23 * k)]
    #          [(a31 * k), (a32 * k), (a33 * k)]]
    # fmt: off
    expected = np.array([[ 0,  3,  6],
                         [ 9, 12, 15],
                         [18, 21, 24]])
    # fmt: on
    assert np.all(actual == expected)


def test_broadcastable_arrays() -> None:
    """Input arrays do not need to have the same number of dimensions.
    The resulting array will have the same number of dimensions as the input array
    with the greatest number of dimensions
    """
    # spell-checker:words broadcastable

    # fmt: off
    A = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    # fmt: on

    # B[:,0] is broadcast to the other columns,

    B = np.array([[3, 5, 7]])
    assert A.shape == (3, 3)
    assert B.shape == (1, 3)

    actual = A * B

    # A * B = [[(a11 * b1), (a12 * b2), (a13 * b3)]
    #          [(a21 * b1), (a22 * b2), (a23 * b3)]
    #          [(a31 * b1), (a32 * b2), (a33 * b3)]]
    # fmt: off
    expected = np.array([[ 0,  5, 14],
                         [ 9, 20, 35],
                         [18, 35, 56]])
    # fmt: on
    assert np.all(actual == expected)
    assert actual.shape == (3, 3)

    # B[0,:] is broadcast to the other rows.

    # fmt: off
    B = np.array([[3],
                  [5],
                  [7]])
    # fmt: on
    assert A.shape == (3, 3)
    assert B.shape == (3, 1)

    actual = A * B

    # A * B = [[(a11 * b11), (a12 * b11), (a13 * b11)]
    #          [(a21 * b21), (a22 * b21), (a23 * b21)]
    #          [(a31 * b31), (a32 * b31), (a33 * b31)]]
    # fmt: off
    expected = np.array([[ 0,  3,  6],
                         [15, 20, 25],
                         [42, 49, 56]])
    # fmt: on
    assert np.all(actual == expected)
    assert actual.shape == (3, 3)

    # B[:] is broadcast to every row, and finally.

    B = np.array([3, 5, 7])
    assert A.shape == (3, 3)
    assert B.shape == (3,)

    actual = A * B

    # A * B = [[(a11 * b1), (a12 * b2), (a13 * b3)]
    #          [(a21 * b1), (a22 * b2), (a23 * b3)]
    #          [(a31 * b1), (a32 * b2), (a33 * b3)]]
    # fmt: off
    expected = np.array([[ 0,  5, 14],
                         [ 9, 20, 35],
                         [18, 35, 56]])
    # fmt: on
    assert np.all(actual == expected)
    assert actual.shape == (3, 3)


def test_do_not_broadcast() -> None:
    """Here are examples of shapes that do not broadcast."""

    # fmt: off
    A = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
    # fmt: on

    # (3,3) * (4,)

    B = np.array([3, 5, 7, 11])
    assert A.shape == (3, 3)
    assert B.shape == (4,)

    with pytest.raises(ValueError) as e:
        A * B
    assert "operands could not be broadcast together with shapes" in str(e.value)

    # (3,3) * (2,3)

    # fmt: off
    B = np.array([[0, 1, 2],
                  [6, 7, 8]])
    # fmt: on
    assert A.shape == (3, 3)
    assert B.shape == (2, 3)

    with pytest.raises(ValueError) as e:
        A * B
    assert "operands could not be broadcast together with shapes" in str(e.value)

    # (3,3) * (3,4)

    # fmt: off
    B = np.array([[0, 1, 2, 0],
                  [3, 4, 5, 0],
                  [6, 7, 8, 0]])
    # fmt: on
    assert A.shape == (3, 3)
    assert B.shape == (3, 4)

    with pytest.raises(ValueError) as e:
        A * B
    assert "operands could not be broadcast together with shapes" in str(e.value)
