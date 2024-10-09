import numpy as np


class TestIndexing:
    # fmt: off
    matrix = np.array([[  0,  1,  2,  3,  4],
                       [  5,  6,  7,  8,  9],
                       [ 10, 11, 12, 13, 14],
                       [ 15, 16, 17, 18, 19],
                       [ 20, 21, 22, 23, 24]])
    # fmt: on

    def test_basic_indexing(self) -> None:
        """Single element indexing."""

        # fmt: off
        assert np.all(self.matrix[2]
                        == np.array([10, 11, 12, 13, 14]))
        assert np.all(self.matrix[-2]
                        == np.array([15, 16, 17, 18, 19]))
        # fmt: on
        assert np.all(self.matrix[2, 2] == 12)
        assert np.all(self.matrix[2, -2] == 13)
        assert np.all(self.matrix[2, 2] == self.matrix[2][2])
        assert np.all(self.matrix[2, -2] == self.matrix[2][-2])

    def test_basic_slicing(self) -> None:
        """Slicing and striding.

        The basic slice syntax is `start:stop:step`
        """

        # fmt: off
        assert np.all(self.matrix[1:2]
                        == np.array([5, 6, 7, 8, 9]))
        assert np.all(self.matrix[1:-2]
                        == np.array([[ 5,  6,  7,  8,  9],
                                     [10, 11, 12, 13, 14]]))

        assert np.all(self.matrix[-1:2] == np.empty((0, 5)))
        assert np.all(self.matrix[-1:2:-1]
                        == np.array([[20, 21, 22, 23, 24],
                                     [15, 16, 17, 18, 19]]))

        assert np.all(self.matrix[1:4:2]
                        == np.array([[ 5,  6,  7,  8,  9],
                                     [15, 16, 17, 18, 19]]))
        assert np.all(self.matrix[1:4:2, 3:5]
                        == np.array([[ 8,  9],
                                     [18, 19]]))

        assert np.all(self.matrix[::-1]
                        == np.array([[20, 21, 22, 23, 24],
                                     [15, 16, 17, 18, 19],
                                     [10, 11, 12, 13, 14],
                                     [ 5,  6,  7,  8,  9],
                                     [ 0,  1,  2,  3,  4]]))

        assert np.all(self.matrix[::-1, ::-1]
                        == np.array([[24, 23, 22, 21, 20],
                                     [19, 18, 17, 16, 15],
                                     [14, 13, 12, 11, 10],
                                     [ 9,  8,  7,  6,  5],
                                     [ 4,  3,  2,  1,  0]]))

        assert np.all(self.matrix[1, :]
                        == np.array([5, 6, 7, 8, 9]))
        assert np.all(self.matrix[1, ...]
                        == np.array([5, 6, 7, 8, 9]))
        assert np.all(self.matrix[:, 1]
                        == np.array([1, 6, 11, 16, 21]))
        assert np.all(self.matrix[..., 1]
                        == np.array([1, 6, 11, 16, 21]))
        # fmt: on

    def test_assigning_values(self) -> None:
        """Assigning values to indexed arrays."""

        matrix = np.arange(25).reshape((5, 5))
        matrix[1:3] = 100

        # fmt: off
        assert np.all(matrix
                      == np.array([[  0,   1,   2,   3,   4],
                                   [100, 100, 100, 100, 100],
                                   [100, 100, 100, 100, 100],
                                   [ 15,  16,  17,  18,  19],
                                   [ 20,  21,  22,  23,  24]]))
        # fmt: on

        matrix = np.arange(25).reshape((5, 5))
        matrix[:, 2:4] = 200

        # fmt: off
        assert np.all(matrix
                      == np.array([[  0,   1, 200, 200,   4],
                                   [  5,   6, 200, 200,   9],
                                   [ 10,  11, 200, 200,  14],
                                   [ 15,  16, 200, 200,  19],
                                   [ 20,  21, 200, 200,  24]]))
        # fmt: on
