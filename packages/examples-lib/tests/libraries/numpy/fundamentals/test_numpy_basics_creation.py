"""This test is for learning to Array creation from NumPy fundamentals section of the NumPy User Guide.

References:
    - https://numpy.org/doc/stable/user/basics.creation.html
"""

from collections.abc import Generator
from pathlib import Path

import numpy as np
import pytest


def test_numpy_from_sequence() -> None:
    """1) Converting Python sequences to NumPy arrays."""
    a1D = np.array([1, 2, 3, 4])
    assert isinstance(a1D, np.ndarray)
    assert a1D.ndim == 1
    # spell-checker:words ndim

    a2D = np.array([[1, 2], [3, 4]])
    assert isinstance(a2D, np.ndarray)
    assert a2D.ndim == 2

    a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    assert isinstance(a3D, np.ndarray)
    assert a3D.ndim == 3

    # When values do not fit and you are using a dtype, NumPy may raise an error:
    with pytest.raises(OverflowError) as e:
        np.array([127, 128, 129], dtype=np.int8)
    assert "Python integer 128 out of bounds for int8" in str(e.value)

    # When when you perform operations with two arrays of the same dtype:
    a = np.array([2, 3, 4], dtype=np.uint32)
    b = np.array([5, 6, 7], dtype=np.uint32)
    c_unsigned32 = a - b
    assert c_unsigned32.dtype == np.uint32

    # When you perform operations with different dtype:
    c_signed32 = a - b.astype(np.int32)
    # spell-checker:words astype
    assert c_signed32.dtype == np.int64


def test_numpy_1d_array_creation_functions() -> None:
    """2) Intrinsic NumPy array creation functions.

    1 - 1D array creation functions
    """
    # numpy.arange

    assert np.all(np.arange(10) == np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert np.all(np.arange(2, 10, dtype=float) == np.array([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]))
    assert np.allclose(np.arange(2, 3, 0.1), np.array([2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]))
    # spell-checker:words allclose

    # numpy.linspace

    assert np.all(np.linspace(1.0, 4.0, 6) == np.array([1.0, 1.6, 2.2, 2.8, 3.4, 4.0]))


def test_numpy_2d_array_creation_functions() -> None:
    """2) Intrinsic NumPy array creation functions.

    2 - 2D array creation functions
    """
    # numpy.eye

    # fmt: off
    assert np.all(np.eye(3) == np.array(
        [[1.0, 0.0, 0.0],
         [0.0, 1.0, 0.0],
         [0.0, 0.0, 1.0]]))
    assert np.all(np.eye(3, 5) == np.array(
        [[1.0, 0.0, 0.0, 0.0, 0.0],
         [0.0, 1.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 1.0, 0.0, 0.0]]))
    # fmt: on

    # numpy.diag

    # fmt: off
    assert np.all(np.diag([1, 2, 3]) == np.array(
        [[1, 0, 0],
         [0, 2, 0],
         [0, 0, 3]]))
    assert np.all(np.diag([1, 2, 3], 1) == np.array(
        [[0, 1, 0, 0],
         [0, 0, 2, 0],
         [0, 0, 0, 3],
         [0, 0, 0, 0]]))
    assert np.all(np.diag(np.array([[1, 2], [3, 4]])) == np.array([1, 4]))
    # fmt: on

    # numpy.vander

    # fmt: off
    assert np.all(np.vander(np.linspace(0, 2, 5), 2) == np.array(
        [[0.0, 1.0],
         [0.5, 1.0],
         [1.0, 1.0],
         [1.5, 1.0],
         [2.0, 1.0]]))
    assert np.all(np.vander([1, 2, 3, 4], 2) == np.array(
        [[1, 1],
         [2, 1],
         [3, 1],
         [4, 1]]))
    assert np.all(np.vander((1, 2, 3, 4), 4) == np.array(
        [[ 1,  1,  1,  1],
         [ 8,  4,  2,  1],
         [27,  9,  3,  1],
         [64, 16,  4,  1]]))
    # fmt: on
    # spell-checker:words vander


def test_numpy_general_creation_functions() -> None:
    """2) Intrinsic NumPy array creation functions.

    3 - general ndarray creation functions
    """
    # numpy.zeros

    # fmt: off
    assert np.all(np.zeros((2, 3)) == np.array(
        [[0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0]]))
    assert np.all(np.zeros((2, 3, 2)) == np.array(
        [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
         [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]])
    )
    # fmt: on

    # numpy.ones

    # fmt: off
    assert np.all(np.ones((2, 3)) == np.array(
        [[1., 1., 1.],
         [1., 1., 1.]]))
    assert np.all(np.ones((2, 3, 2)) == np.array(
        [[[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]],
         [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]]))
    # fmt: on

    # numpy.random

    rnd1 = np.random.default_rng(42).random(size=(2, 3))
    assert np.all(rnd1.shape == (2, 3))
    assert np.all(rnd1 >= 0.0) and np.all(rnd1 <= 1.0)

    rnd2 = np.random.default_rng(42).random((2, 3, 2))
    assert np.all(rnd2.shape == (2, 3, 2))
    assert np.all(rnd2 >= 0.0) and np.all(rnd1 <= 1.0)

    # numpy.indices

    # fmt: off
    assert np.all(np.indices((3, 3)) == np.array(
        [[[0, 0, 0], [1, 1, 1], [2, 2, 2]],
         [[0, 1, 2], [0, 1, 2], [0, 1, 2]]])
    )
    # fmt: on


def test_numpy_from_existing_arrays() -> None:
    """3) Replicating, joining, or mutating existing arrays."""
    # view
    a = np.array([1, 2, 3, 4, 5, 6])
    b = a[:2]
    b += 1
    assert np.all(a == np.array([2, 3, 3, 4, 5, 6]))
    assert np.all(b == np.array([2, 3]))

    # copy
    a = np.array([1, 2, 3, 4, 5, 6])
    b = a[:2].copy()
    b += 1
    assert np.all(a == np.array([1, 2, 3, 4, 5, 6]))
    assert np.all(b == np.array([2, 3]))

    # numpy.block, numpy.vstack, numpy.hstack
    # spell-checker:words hstack

    A = np.ones((2, 2))
    B = np.eye(2, 2)
    C = np.zeros((2, 2))
    D = np.diag((-3, -4))

    # fmt: off
    assert np.all(np.block([[A, B], [C, D]]) == np.array(
        [[1.0, 1.0, 1.0, 0.0],
         [1.0, 1.0, 0.0, 1.0],
         [0.0, 0.0, -3.0, 0.0],
         [0.0, 0.0, 0.0, -4.0]])
    )

    assert np.all(np.vstack(([A, B], [C, D])) == np.array(
        [[[1.0, 1.0], [1.0, 1.0]],
         [[1.0, 0.0], [0.0, 1.0]],
         [[0.0, 0.0], [0.0, 0.0]],
         [[-3.0, 0.0], [0.0, -4.0]]])
    )

    assert np.all(np.hstack(([A, B], [C, D])) == np.array(
        [[[1.0, 1.0], [1.0, 1.0], [0.0, 0.0], [0.0, 0.0]],
         [[1.0, 0.0], [0.0, 1.0], [-3.0, 0.0], [0.0, -4.0]]])
    )
    # fmt: on


@pytest.fixture(scope="function")
def bin_file(tmp_path: Path) -> Generator[Path]:
    array = np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 4.0], [3.0, 9.0]])
    path = tmp_path / "sample.npy"
    np.save(path, array)
    yield path
    path.unlink(missing_ok=True)


def test_numpy_from_binary_file(bin_file: str) -> None:
    """4) Reading arrays from disk, either from standard or custom formats.

    Standard binary formats:
    """
    actual = np.load(bin_file, mmap_mode="r")
    assert np.all(actual == np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 4.0], [3.0, 9.0]]))


@pytest.fixture(scope="function")
def ascii_file(tmp_path: Path) -> Generator[Path]:
    array = np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 4.0], [3.0, 9.0]])
    path = tmp_path / "sample.csv"
    np.savetxt(path, array, delimiter=",", header="ｘ,ｙ", encoding="utf-8_sig", fmt="%.3f")  # use BOM
    # spell-checker:words savetxt
    yield path
    path.unlink(missing_ok=True)


def test_numpy_from_ascii_file(ascii_file: Path) -> None:
    """4) Reading arrays from disk, either from standard or custom formats.

    Common ASCII formats:
    """
    actual = np.loadtxt(ascii_file, delimiter=",", skiprows=1, encoding="utf-8_sig")  # use BOM
    # spell-checker:words loadtxt
    # spell-checker:words skiprows

    assert np.all(actual == np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 4.0], [3.0, 9.0]]))


def test_numpy_from_raw_bytes() -> None:
    """5) Creating arrays from raw bytes through the use of strings or buffers."""
    pass


def test_numpy_use_library_functions() -> None:
    """6) Use of special library functions (e.g., SciPy, pandas, and OpenCV)."""
    pass
