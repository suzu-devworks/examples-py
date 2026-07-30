"""This test is for learning to Copies and views from NumPy fundamentals section of the NumPy User Guide.

References:
    - https://numpy.org/doc/stable/user/basics.copies.html
"""

import numpy as np


def test_indexing_operations() -> None:
    """Indexing operations."""
    # Basic indexing always creates views
    x = np.arange(10)
    y = x[1:3]  # creates a view
    x[1:3] = [10, 11]

    assert np.all(x == np.array([0, 10, 11, 3, 4, 5, 6, 7, 8, 9]))
    assert np.all(y == np.array([10, 11]))

    # Advanced indexing always makes a copy
    x = np.arange(9).reshape(3, 3)
    y = x[[1, 2]]  # creates a copy
    x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]

    assert np.all(x == np.array([[0, 1, 2], [10, 11, 12], [13, 14, 15]]))
    assert np.all(y == np.array([[3, 4, 5], [6, 7, 8]]))


def test_other_operations() -> None:
    """Other operations."""
    a = np.arange(24).reshape(2, 3, 4)

    # makes the array non-contiguous
    b = a.transpose(2, 1, 0)
    assert b.base is not None  # `b` is a view of `a`

    # The `numpy.reshape` function creates a view where possible or a copy otherwise.
    a1 = a.reshape(24)
    b1 = b.reshape(24)

    assert a1.base is not None  # `a1` is a view of `a`
    # It seems that even with something like `transpose`, you can still create a view.
    # assert b1.base is None  # `b1` is a copy of `b`
    assert b1.base is not None  # `b1` is a view of `b` ???

    # `numpy.ravel` returns a contiguous flattened view of the array wherever possible.
    a2 = a.ravel()
    b2 = b.ravel()

    assert a2.base is not None  # `a2` is a view of `a`
    assert b2.base is None  # `b2` is a copy of `b`

    # `ndarray.flatten` always returns a flattened copy of the array.
    a3 = a.flatten()
    b3 = b.flatten()

    assert a3.base is None  # `a3` is a copy of `a`
    assert b3.base is None  # `b3` is a copy of `b`

    # To guarantee a view in most cases, `x.reshape(-1)` may be preferable.
    a4 = a.reshape(-1)
    b4 = b.reshape(-1)

    assert a4.base is not None  # `a4` is a view of `a`
    assert b4.base is not None  # `b4` is a view of `b


def test_how_to_tell_if_view_or_copy() -> None:
    """How to tell if the array is a view or a copy."""
    # The base attribute of the ndarray makes it easy to tell if an array is a view or a copy:
    x = np.arange(9)

    # .reshape() creates a view:
    y = x.reshape(3, 3)
    assert y.base is not None
    assert np.all(y.base == np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]))

    # advanced indexing creates a copy:
    z = y[[2, 1]]
    assert z.base is None
