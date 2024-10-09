import numpy as np


class TestBroadcasting:
    def test_basic_broadcast(self) -> None:
        """The simplest broadcasting example occurs
        when an array and a scalar value are combined in an operation.
        """

        # The two arrays have exactly the same shape.
        a = np.array([1.0, 2.0, 3.0])
        b = np.array([2.0, 2.0, 2.0])
        actual = a * b

        assert np.all(actual == np.array([2.0, 4.0, 6.0]))

        # A scalar value.
        a = np.array([1.0, 2.0, 3.0])
        b = 2
        actual = a * b

        assert np.all(actual == np.array([2.0, 4.0, 6.0]))

    def test_when_dimensions_is_different(self) -> None:
        """Input arrays do not need to have the same number of dimensions.
        The resulting array will have the same number of dimensions as the input array
        with the greatest number of dimensions
        """
        a = np.arange(9).reshape(3, 3)
        b = np.array([3, 5, 7])
        actual = a * b

        assert a.shape == (3, 3)
        assert b.shape == (3,)

        # fmt: off
        assert np.all(actual == np.array([[ 0,  5, 14],
                                          [ 9, 20, 35],
                                          [18, 35, 56]]))
        # fmt: on1

        a = np.arange(9).reshape(3, 3)
        b = np.array([[3], [5], [7]])
        actual = a * b

        assert a.shape == (3, 3)
        assert b.shape == (3, 1)

        # fmt: off
        assert np.all(actual == np.array([[ 0,  3,  6],
                                          [15, 20, 25],
                                          [42, 49, 56]]))
        # fmt: on1
