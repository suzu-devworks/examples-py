"""This test is for learning how to create mathematical matrices.

References:
    - https://numpy.org/doc/stable/reference/routines.array-creation.html
"""

import numpy as np
import numpy.linalg as LA


def test_using_numpy_zeros() -> None:
    """Return a new array of given shape and type, filled with zeros.

    `numpy.zeros(shape, dtype=float, order='C', *, like=None)`
    """
    actual = np.zeros((3, 3))

    # fmt: off
    expected = np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])
    # fmt: on

    # NumPy comparisons with Python integers or mixed precision integers always return the correct result.
    # The inputs will never be cast in a way which loses precision.
    assert np.all(actual == expected)
    assert np.array_equal(actual, expected)

    # Determinant: (0*0*0) + (0) + (0) - (0) - (0) - (0) = 0
    assert LA.det(actual) == 0


def test_using_numpy_ones() -> None:
    """Return a new array of given shape and type, filled with ones.

    `numpy.ones(shape, dtype=None, order='C', *, device=None, like=None)`
    """
    actual = np.ones((3, 3))

    # fmt: off
    expected = np.array([[1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (1*1*1) + (1) + (1) - (1) - (1) - (1) = 0
    assert LA.det(actual) == 0


def test_using_numpy_full() -> None:
    """Return a new array of given shape and type, filled with fill_value.

    `numpy.full(shape, fill_value, dtype=None, order='C', *, device=None, like=None)`
    """
    actual = np.full((3, 3), 11.1)

    # fmt: off
    expected = np.array([[11.1, 11.1, 11.1],
                         [11.1, 11.1, 11.1],
                         [11.1, 11.1, 11.1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (11.1*11.1*11.1) + (1367.63099...) + (...) - (...) - (...) - (...) = 0
    assert LA.det(actual) == 0


def test_using_numpy_eye() -> None:
    """Return a 2-D array with ones on the diagonal and zeros elsewhere.

    `numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, device=None, like=None)`
    """
    actual = np.eye(3)

    # fmt: off
    expected = np.array([[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (1*1*1) + (0*0*0) + (0*0*0) - (1*0*0) - (0*0*1) - (1*0*0) = 1
    assert LA.det(actual) == 1


def test_using_numpy_identity() -> None:
    """Return the identity array.

    `numpy.identity(n, dtype=None, *, like=None)`
    """
    actual = np.identity(3)

    # fmt: off
    expected = np.array([[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (1*1*1) + (0*0*0) + (0*0*0) - (1*0*0) - (0*0*1) - (1*0*0) = 1
    assert LA.det(actual) == 1


def test_using_numpy_tri() -> None:
    """An array with ones at and below the given diagonal and zeros elsewhere.

    `numpy.tri(N, M=None, k=0, dtype=<class 'float'>, *, like=None)`
    """
    actual = np.tri(3)

    # fmt: off
    expected = np.array([[1, 0, 0],
                         [1, 1, 0],
                         [1, 1, 1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (1*1*1) + (0*0*1) + (0*1*1) - (0*1*1) - (0*1*1) - (1*0*1) = 1
    assert LA.det(actual) == 1


def test_using_numpy_tril() -> None:
    """Lower triangle of an array.

    `numpy.tril ( m、 k = 0 )`
    """
    # spell-checker:words tril
    actual = np.tril(np.ones((3, 3)))

    # fmt: off
    expected = np.array([[1, 0, 0],
                         [1, 1, 0],
                         [1, 1, 1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (1*1*1) + (0*0*1) + (0*1*1) - (0*1*1) - (0*1*1) - (1*0*1) = 1
    assert LA.det(actual) == 1


def test_using_numpy_triu() -> None:
    """Upper triangle of an array.

    `numpy.triu(m, k=0)`
    """
    # spell-checker:words triu
    actual = np.triu(np.ones((3, 3)))

    # fmt: off
    expected = np.array([[1, 1, 1],
                         [0, 1, 1],
                         [0, 0, 1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (1*1*1) + (1*1*0) + (1*0*0) - (1*1*0) - (1*0*1) - (1*1*0) = 1
    assert LA.det(actual) == 1


def test_using_numpy_diag() -> None:
    """Extract a diagonal or construct a diagonal array.

    `numpy.diag(v, k=0)`
    """
    actual = np.diag([1, 2, 3])

    # fmt: off
    expected = np.array([[1, 0, 0],
                         [0, 2, 0],
                         [0, 0, 3]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: (1*2*3) + (0*0*0) + (0*0*0) - (0*2*0) - (0*0*3) - (1*0*0) = 6
    assert LA.det(actual) == 6


def test_using_numpy_diagflat() -> None:
    """Create a two-dimensional array with the flattened input as a diagonal.

    `numpy.diagflat(v, k=0)`
    """
    # spell-checker:words diagflat
    actual = np.diagflat([[1, 2], [3, 4]])

    # fmt: off
    expected = np.array([[1, 0, 0, 0],
                         [0, 2, 0, 0],
                         [0, 0, 3, 0],
                         [0, 0, 0, 4]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: 1 * ((2*3*4) + (0*0*0) + (0*0*0) - (0*3*0) - (0*0*4) - (2*0*0))
    #               - 0 * ((0*3*4) + (0*0*0) + (0*0*0) - (0*3*0) - (0*0*4) - (0*0*0))
    #               + 0 * ((0*0*4) + (0*0*0) + (0*2*0) - (0*0*0) - (0*2*4) - (0*0*0))
    #               - 0 * ((0*0*0) + (0*0*0) + (0*2*3) - (0*0*0) - (0*2*0) - (0*3*0))
    #               = 24
    # Since float64 values ​​are too fine-grained for array_equal to succeed, we perform a rough comparison.
    assert np.isclose(LA.det(actual), 24)


def test_using_numpy_vander() -> None:
    """Return a copy of an array with the elements below the k-th diagonal zeroed.

    `numpy.vander(x, N=None, increasing=False)`
    """
    # spell-checker:words vander
    actual = np.vander(np.array([0, 1, 2, 3]))

    # fmt: off
    expected = np.array([[0,  0,  0,  1],
                         [1,  1,  1,  1],
                         [8,  4,  2,  1],
                         [27, 9,  3,  1]])
    # fmt: on
    assert np.array_equal(actual, expected)

    # Determinant: 0 * ((1*2*1) + (1*1*9) + (1*4*3) - (1*2*9) - (1*4*1) - (1*1*3))
    #               - 1 * ((0*2*1) + (0*1*9) + (1*4*3) - (1*2*9) - (0*4*1) - (0*1*3))
    #               + 8 * ((0*1*1) + (0*1*9) + (1*1*3) - (1*1*9) - (0*1*1) - (0*1*3))
    #               - 27 * ((0*1*1) + (0*1*4) + (1*1*2) - (1*1*4) - (0*1*1) - (0*1*2))
    #               = -1 * (12 - 18) + 8 * (3 - 9) - 27 * (2 - 4)
    #               = 6 - 48 + 54
    #               = 12
    assert np.isclose(LA.det(actual), 12)
