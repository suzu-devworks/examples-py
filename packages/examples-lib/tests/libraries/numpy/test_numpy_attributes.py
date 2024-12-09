"""This test is for learning basic attribute values of ndarray.

References:
    - https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes
"""

from typing import Any

import numpy as np
import numpy.typing as npt
import pytest

ndarray = npt.NDArray[Any]


@pytest.fixture(scope="module")
def matrix() -> ndarray:
    return np.array([[1.0, 2.0, 3.0], [11.0, 12.0, 13.0]])


def test_gets_ndim(matrix: ndarray) -> None:
    """Number of array dimensions."""
    assert matrix.ndim == 2
    # spell-checker:words ndim


def test_gets_shape(matrix: ndarray) -> None:
    """Tuple of array dimensions."""
    assert matrix.shape == (2, 3)


def test_gets_size(matrix: ndarray) -> None:
    """Number of elements in the array."""
    assert matrix.size == 6


def test_gets_dtype(matrix: ndarray) -> None:
    """An object that describes the type of the elements in the array."""
    assert matrix.dtype == np.float64
    # spell-checker:words dtype


def test_gets_itemsize(matrix: ndarray) -> None:
    """Length of one array element in bytes."""
    assert matrix.itemsize == 8
    # spell-checker:words itemsize


def test_gets_data(matrix: ndarray) -> None:
    """Python buffer object pointing to the start of the array’s data."""
    assert matrix.data != memoryview(b"abcdef")


def test_gets_flags(matrix: ndarray) -> None:
    """Information about the memory layout of the array."""
    # The data is in a single, C-style contiguous segment
    assert matrix.flags["C_CONTIGUOUS"]
    # The data is in a single, Fortran-style contiguous segment.
    assert not matrix.flags["F_CONTIGUOUS"]
    # The array owns the memory it uses or borrows it from another object.
    # spell-checker:words OWNDATA
    assert matrix.flags["OWNDATA"]
    # The data area can be written to.
    assert matrix.flags["WRITEABLE"]
    # The data and all elements are aligned appropriately for the hardware.
    assert matrix.flags["ALIGNED"]
    # This array is a copy of some other array.
    # spell-checker:words WRITEBACKIFCOPY
    assert not matrix.flags["WRITEBACKIFCOPY"]
