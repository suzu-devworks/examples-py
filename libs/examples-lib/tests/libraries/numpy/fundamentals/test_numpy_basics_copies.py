"""This test is for learning to Copies and views from NumPy fundamentals section of the NumPy User Guide.

References:
    - https://numpy.org/doc/stable/user/basics.copies.html
"""

import numpy as np
import pytest


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
    # The numpy.reshape function creates a view where possible or a copy otherwise
    x = np.ones((2, 3))
    y = x.T  # makes the array non-contiguous

    z = y.view()
    with pytest.raises(AttributeError) as e:
        z.shape = 6
    assert "Incompatible shape for in-place modification." in str(e.value)


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
