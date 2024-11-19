"""This test is for learning how to create basic arrays.

References:
    - https://numpy.org/doc/stable/reference/routines.array-creation.html
"""

import numpy as np


def test_using_numpy_arange() -> None:
    """Return evenly spaced values within a given interval.

    `numpy.arange([start, ]stop, [step, ]dtype=None, *, device=None, like=None)`
    """
    actual = np.arange(10)

    expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert np.array_equal(actual, expected)

    actual = np.arange(2, 10, dtype=float)

    expected = np.array([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
    assert np.array_equal(actual, expected)

    actual = np.arange(15, 100, 3)

    # fmt: off
    expected = np.array([15, 18, 21, 24, 27, 30, 33, 36, 39, 42,
                         45, 48, 51, 54, 57, 60, 63, 66, 69, 72,
                         75, 78, 81, 84, 87, 90, 93, 96, 99])
    # fmt: on
    assert np.array_equal(actual, expected)


def test_using_numpy_linspace() -> None:
    """Return evenly spaced numbers over a specified interval.

    `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0, *, device=None)`
    """
    # spell-checker:words retstep

    actual = np.linspace(1, 4, 10)

    # fmt: off
    expected =  np.array([
        1.0,
        1.33333333,
        1.66666667,
        2.0,
        2.33333333,
        2.66666667,
        3.0,
        3.33333333,
        3.66666667,
        4.0
    ]),
    # fmt: on
    # Since float64 values ​​are too fine-grained for array_equal to succeed, we perform a rough comparison.
    assert np.all(np.isclose(actual, expected))


def test_using_numpy_logspace() -> None:
    """Return numbers spaced evenly on a log scale.

    `numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)`
    """
    # spell-checker:words logspace

    # --- :math:`\log_{10} x` base 10 logarithm ---
    actual = np.logspace(1, 4, 10)

    # fmt: off
    expected = np.array([
        10.0,
        21.5443469,
        46.41588834,
        100.0,
        215.443469,
        464.15888336,
        1000.0,
        2154.43469003,
        4641.58883361,
        10000.0,
    ])
    # fmt: on
    assert np.all(np.isclose(actual, expected))

    # --- :math:`\log_{2} x` base 2 logarithm ---
    actual = np.logspace(1, 4, 10, base=2)

    # fmt: off
    expected = np.array([
        2.0,
        2.5198421,
        3.1748021,
        4.0,
        5.0396842,
        6.34960421,
        8.0,
        10.0793684,
        12.69920842,
        16.0
    ])
    # fmt: on
    assert np.all(np.isclose(actual, expected))

    # --- :math:`\log_e x` base e logarithm ---
    actual = np.logspace(1, 4, 10, base=np.e)

    # fmt: off
    expected = np.array([
        2.71828183,
        3.79366789,
        5.29449005,
        7.3890561,
        10.3122585,
        14.3919161,
        20.08553692,
        28.03162489,
        39.121284,
        54.59815003,
    ])
    # fmt: on
    assert np.all(np.isclose(actual, expected))


def test_using_numpy_geomspace() -> None:
    """Return numbers spaced evenly on a log scale (a geometric progression).

    This is similar to logspace, but with endpoints specified directly.

    `numpy.geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0)`
    """
    # spell-checker:words geomspace

    actual = np.geomspace(1, 4, 10)

    # fmt: off
    expected = np.array([
        1.0,
        1.16652904,
        1.36079,
        1.58740105,
        1.85174942,
        2.16011948,
        2.5198421,
        2.93946898,
        3.42897593,
        4.0
    ])
    # fmt: on
    assert np.all(np.isclose(actual, expected))


def test_using_numpy_random_randint() -> None:
    """Return random integers from low (inclusive) to high (exclusive).

    `random.randint(low, high=None, size=None, dtype=int)`
    """
    actual = np.random.randint(1, 10, size=(3, 3))

    assert actual.shape == (3, 3)
    assert actual.dtype == int


def test_using_numpy_random_random() -> None:
    """Return random floats in the half-open interval [0.0, 1.0).
    Alias for random_sample to ease forward-porting to the new random API.

    `random.random(size=None)`
    """
    actual = np.random.random(size=(3, 3))

    assert actual.shape == (3, 3)
    assert actual.dtype == float
