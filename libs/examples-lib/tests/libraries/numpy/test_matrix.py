import numpy as np
import numpy.linalg as LA


class TestMatrix:
    def test_create_zero_matrix(self) -> None:
        """Return a new array of given shape and type, filled with zeros.

        `numpy.zeros(shape, dtype=float, order='C', *, like=None)`
        """
        # fmt: off
        expected = np.array([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]])
        # fmt: on
        actual = np.zeros((3, 3))

        # NumPy comparisons with Python integers or mixed precision integers always return the correct result.
        # The inputs will never be cast in a way which loses precision.
        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

        # Determinant: (0*0*0) + (0) + (0) - (0) - (0) - (0) = 0
        assert LA.det(actual) == 0

    def test_create_matrix_with_ones(self) -> None:
        """Return a new array of given shape and type, filled with ones.

        `numpy.ones(shape, dtype=None, order='C', *, device=None, like=None)`
        """
        # fmt: off
        expected = np.array([[1, 1, 1],
                             [1, 1, 1],
                             [1, 1, 1]])
        # fmt: on
        actual = np.ones((3, 3))

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

        # Determinant: (1*1*1) + (1) + (1) - (1) - (1) - (1) = 0
        assert LA.det(actual) == 0

    def test_create_matrix_with_any(self) -> None:
        """Return a new array of given shape and type, filled with fill_value.

        `numpy.full(shape, fill_value, dtype=None, order='C', *, device=None, like=None)`
        """
        # fmt: off
        expected = np.array([[11.1, 11.1, 11.1],
                             [11.1, 11.1, 11.1],
                             [11.1, 11.1, 11.1]])
        # fmt: on
        actual = np.full((3, 3), 11.1)

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

        # Determinant: (11.1*11.1*11.1) + (1367.63099...) + (...) - (...) - (...) - (...) = 0
        assert LA.det(actual) == 0

    def test_create_identity_matrix(self) -> None:
        """Return the identity array.

        `numpy.identity(n, dtype=None, *, like=None)`
        `numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, device=None, like=None)`
        """
        # fmt: off
        expected = np.array([[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]])
        # fmt: on
        actual = np.identity(3)

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

        # Determinant: (1*1*1) + (0*0*0) + (0*0*0) - (1*0*0) - (0*0*1) - (0*1*0) = 1
        assert LA.det(actual) == 1

        matrix = np.eye(3)
        assert np.all(expected == matrix)

    def test_create_lower_triangular_matrix(self) -> None:
        """Return a copy of an array with elements above the k-th diagonal zeroed.

        `numpy.tri(N, M=None, k=0, dtype=<class 'float'>, *, like=None)`
        `numpy.tril ( m、 k = 0 )`
        """
        # fmt: off
        expected = np.array([[1, 0, 0],
                             [1, 1, 0],
                             [1, 1, 1]])
        # fmt: on
        actual = np.tri(3)

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

        # Determinant: (1*1*1) + (0*0*1) + (0*1*1) - (1*0*1) - (0*1*1) - (0*1*1) = 1
        assert LA.det(actual) == 1

        # spell-checker:words tril
        actual = np.tril(np.ones((3, 3)))

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

    def test_create_upper_triangular_matrix(self) -> None:
        """Return a copy of an array with the elements below the k-th diagonal zeroed.

        `numpy.triu(m, k=0)`
        """
        # fmt: off
        expected = np.array([[1, 1, 1],
                             [0, 1, 1],
                             [0, 0, 1]])
        # fmt: on
        # spell-checker:words triu
        actual = np.triu(np.ones((3, 3)))

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

        # Determinant: (1*1*1) + (1*1*0) + (1*0*0) - (1*1*0) - (1*0*1) - (1*1*0) = 1
        assert LA.det(actual) == 1

    def test_create_diagonal_matrix(self) -> None:
        """Construct a diagonal array.

        `numpy.diag(v, k=0)`
        """
        # fmt: off
        expected = np.array([[1, 0, 0],
                             [0, 2, 0],
                             [0, 0, 3]])
        # fmt: on
        actual = np.diag([1, 2, 3])

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)

        # Determinant: (1*2*3) + (0*0*0) + (0*0*0) - (1*0*0) - (0*0*3) - (0*2*0) = 6
        assert LA.det(actual) == 6

    def test_create_vandermonde_matrix(self) -> None:
        """Return a copy of an array with the elements below the k-th diagonal zeroed.

        `numpy.vander(x, N=None, increasing=False)`
        """
        # spell-checker:words vander
        # spell-checker:words vandermonde
        # fmt: off
        expected = np.array([[0, 0, 0, 1],
                             [1, 1, 1, 1],
                             [8, 4, 2, 1],
                             [27, 9, 3, 1]])
        # fmt: on
        # spell-checker:words triu
        actual = np.vander(np.array([0, 1, 2, 3]))

        assert np.all(expected == actual)
        assert np.array_equal(expected, actual)
