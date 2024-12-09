"""This test is for learning to Broadcasting from NumPy fundamentals section of the NumPy User Guide.

References:
    - https://numpy.org/doc/stable/user/basics.broadcasting.html
"""

import numpy as np
import pytest


def test_broadcasting_same_shape() -> None:
    """In the simplest case, the two arrays must have exactly the same shape."""
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([2.0, 2.0, 2.0])
    actual = a * b
    assert np.all(actual == np.array([2.0, 4.0, 6.0]))


def test_broadcasting_scalar_value() -> None:
    """The simplest broadcasting example occurs when an array and
    a scalar value are combined in an operation.
    """
    a = np.array([1.0, 2.0, 3.0])
    b = 2.0

    actual = a * b
    assert np.all(actual == np.array([2.0, 4.0, 6.0]))


def test_general_broadcasting_rules() -> None:
    """General broadcasting rules."""
    image = np.random.choice(range(256), size=(256, 256, 3))
    scale = np.array([1, 3, 5])
    result = image * scale
    assert result.shape == (256, 256, 3)

    A = np.random.choice(range(256), size=(8, 1, 6, 1))
    B = np.random.choice(range(256), size=(7, 1, 5))
    result = A * B
    assert result.shape == (8, 7, 6, 5)


def test_broadcastable_arrays() -> None:
    """Broadcastable arrays."""
    # spell-checker:words broadcastable
    x = np.arange(30).reshape(5, 6)

    # a acts like a (5,6) array where a[:,0] is broadcast to the other columns,
    a = np.arange(5).reshape(5, 1)
    actual = x * a
    # fmt: off
    assert np.all(actual == np.array(
        [[  0,   0,   0,   0,   0,   0],
         [  6,   7,   8,   9,  10,  11],
         [ 24,  26,  28,  30,  32,  34],
         [ 54,  57,  60,  63,  66,  69],
         [ 96, 100, 104, 108, 112, 116]]))
    # fmt: on

    # b acts like a (5,6) array where b[0,:] is broadcast to the other rows,
    b = np.arange(6).reshape(1, 6)
    actual = x * b
    # fmt: off
    assert np.all(actual == np.array(
        [[  0,   1,   4,   9,  16,  25],
         [  0,   7,  16,  27,  40,  55],
         [  0,  13,  28,  45,  64,  85],
         [  0,  19,  40,  63,  88, 115],
         [  0,  25,  52,  81, 112, 145]]))
    # fmt: on

    # c acts like a (1,6) array and therefore like a (5,6) array where c[:]
    # is broadcast to every row, and finally,
    c = np.arange(6)
    actual = x * c
    # fmt: off
    assert np.all(actual == np.array(
        [[  0,   1,   4,   9,  16,  25],
         [  0,   7,  16,  27,  40,  55],
         [  0,  13,  28,  45,  64,  85],
         [  0,  19,  40,  63,  88, 115],
         [  0,  25,  52,  81, 112, 145]]))
    # fmt: on

    # d acts like a (5,6) array where the single value is repeated.
    d = 2
    actual = x * d
    # fmt: off
    assert np.all(actual == np.array(
        [[ 0,  2,  4,  6,  8, 10],
         [12, 14, 16, 18, 20, 22],
         [24, 26, 28, 30, 32, 34],
         [36, 38, 40, 42, 44, 46],
         [48, 50, 52, 54, 56, 58]]))
    # fmt: on

    # When a 1-d array is added to a 2-d array:
    # fmt: off
    a = np.array(
        [[ 0.0,  0.0,  0.0],
         [10.0, 10.0, 10.0],
         [20.0, 20.0, 20.0],
         [30.0, 30.0, 30.0]])
    # fmt: on

    b = np.array([1.0, 2.0, 3.0])
    actual = a + b
    # fmt: off
    assert np.all(actual == np.array(
        [[ 1.0,  2.0,  3.0],
         [11.0, 12.0, 13.0],
         [21.0, 22.0, 23.0],
         [31.0, 32.0, 33.0]]))
    # fmt: on

    b = np.array([1.0, 2.0, 3.0, 4.0])
    with pytest.raises(ValueError) as e:
        actual = a + b
    assert "operands could not be broadcast together with shapes" in str(e.value)


def test_example_vector_quantization() -> None:
    """A practical example: vector quantization."""
    observation = np.array([111.0, 188.0])
    # fmt: off
    codes = np.array(
        [[102.0, 203.0],
         [132.0, 193.0],
         [ 45.0, 155.0],
         [ 57.0, 173.0]])
    # fmt: on
    diff = codes - observation  # the broadcast happens here
    dist = np.sqrt(np.sum(diff**2, axis=-1))
    index = np.argmin(dist)
    # spell-checker:words argmin
    assert index == 0
