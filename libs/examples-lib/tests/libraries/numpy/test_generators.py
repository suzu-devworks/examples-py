import numpy as np


class TestGenerator:
    def test_generate_range_numbers(self) -> None:
        """Return evenly spaced values within a given interval.

        `numpy.arange([start, ]stop, [step, ]dtype=None, *, device=None, like=None)`
        """
        expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        actual = np.arange(10)

        assert np.array_equal(expected, actual)

        # fmt: off
        expected = np.array([15, 18, 21, 24, 27, 30, 33, 36, 39, 42,
                             45, 48, 51, 54, 57, 60, 63, 66, 69, 72,
                             75, 78, 81, 84, 87, 90, 93, 96, 99])
        # fmt: on
        actual = np.arange(15, 100, 3)

        assert np.array_equal(expected, actual)

    def test_generate_evenly_interval_numbers(self) -> None:
        """Return evenly spaced numbers over a specified interval.

        `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0, *, device=None)`
        """
        # spell-checker:words retstep
        # fmt: off
        expected = np.array([1.        ,  1.33333333,  1.66666667,  2.        ,  2.33333333,
                             2.66666667,  3.        ,  3.33333333,  3.66666667,  4.])
        # fmt: on
        actual = np.linspace(1, 4, 10)

        # Since float64 values ​​are too fine-grained for array_equal to succeed, we perform a rough comparison.
        # assert np.array_equal(expected, actual)
        assert np.all(np.isclose(expected, actual))

    def test_generate_evenly_interval_log_scales(self) -> None:
        """Return numbers spaced evenly on a log scale.

        `numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)`
        """
        # spell-checker:words logspace

        # --- :math:`\log_{10} x` base 10 logarithm ---
        # fmt: off
        expected = np.array([  10.        ,    21.5443469 ,    46.41588834,   100.        ,
                              215.443469  ,   464.15888336,  1000.        ,  2154.43469003,
                             4641.58883361, 10000.      ])
        # fmt: on
        actual = np.logspace(1, 4, 10)

        # Since float64 values ​​are too fine-grained for array_equal to succeed, we perform a rough comparison.
        # assert np.array_equal(expected, actual)
        assert np.all(np.isclose(expected, actual))

        # --- :math:`\log_{2} x` base 2 logarithm ---
        # fmt: off
        expected = np.array([2.        ,  2.5198421 ,  3.1748021 ,  4.        ,  5.0396842 ,
                             6.34960421,  8.        , 10.0793684 , 12.69920842, 16.   ])
        # fmt: on
        actual = np.logspace(1, 4, 10, base=2)

        assert np.all(np.isclose(expected, actual))

        # --- :math:`\log_e x` base e logarithm ---
        # fmt: off
        expected = np.array([ 2.71828183,  3.79366789,  5.29449005,  7.3890561 , 10.3122585 ,
                             14.3919161 , 20.08553692, 28.03162489, 39.121284  , 54.59815003])
        # fmt: on
        actual = np.logspace(1, 4, 10, base=np.e)

        assert np.all(np.isclose(expected, actual))

    def test_generate_evenly_interval_geometric_scales(self) -> None:
        """Return numbers spaced evenly on a log scale (a geometric progression).

        This is similar to logspace, but with endpoints specified directly.

        `numpy.geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0)`
        """
        # spell-checker:words geomspace
        # fmt: off
        expected = np.array([1.        , 1.16652904, 1.36079   , 1.58740105, 1.85174942,
                             2.16011948, 2.5198421 , 2.93946898, 3.42897593, 4.        ])
        # fmt: on
        actual = np.geomspace(1, 4, 10)

        # Since float64 values ​​are too fine-grained for array_equal to succeed, we perform a rough comparison.
        # assert np.array_equal(expected, actual)
        assert np.all(np.isclose(expected, actual))

    def test_generate_random_integer(self) -> None:
        """.
        `random.randint(low, high=None, size=None, dtype=int)`
        """
        actual = np.random.randint(1, 10, size=(3, 3))

        assert actual.shape == (3, 3)
        assert actual.dtype.name == "int64"

    def test_generate_random_float(self) -> None:
        """Return random floats in the half-open interval [0.0, 1.0).

        `random.random(size=None)`
        `random.random_sample(size=None)`
        """
        actual = np.random.random(size=(3, 3))

        assert actual.shape == (3, 3)
        assert actual.dtype.name == "float64"

        actual = np.random.random_sample(size=(3, 3))

        assert actual.shape == (3, 3)
        assert actual.dtype.name == "float64"
