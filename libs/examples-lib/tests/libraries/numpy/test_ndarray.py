import numpy as np


class TestNdArray:
    matrix = np.array([[1.0, 2.0, 3.0], [11.0, 12.0, 13.0]])

    def test_gets_dimensions_of_axis(self) -> None:
        """Number of array dimensions."""
        assert self.matrix.ndim == 2
        # spell-checker:words ndim

    def test_gets_dimensions_of_array(self) -> None:
        """Tuple of array dimensions."""
        assert self.matrix.shape == (2, 3)

    def test_gets_total_number_of_elements(self) -> None:
        """Number of elements in the array."""
        assert self.matrix.size == 6

    def test_gets_type_of_elements(self) -> None:
        """An object that describes the type of the elements in the array."""
        assert self.matrix.dtype.name == "float64"
        # spell-checker:words dtype

    def test_gets_bytes_of_element(self) -> None:
        """Length of one array element in bytes."""
        assert self.matrix.itemsize == 8
        # spell-checker:words itemsize

    def test_gets_pointer_address_in_c(self) -> None:
        """Python buffer object pointing to the start of the array’s data."""
        assert self.matrix.data != memoryview(b"abcdef")

    def test_gets_flags(self) -> None:
        """Information about the memory layout of the array."""
        # The data is in a single, C-style contiguous segment
        assert self.matrix.flags["C_CONTIGUOUS"]
        # The data is in a single, Fortran-style contiguous segment.
        assert not self.matrix.flags["F_CONTIGUOUS"]
        # The array owns the memory it uses or borrows it from another object.
        # spell-checker:words OWNDATA
        assert self.matrix.flags["OWNDATA"]
        # The data area can be written to.
        assert self.matrix.flags["WRITEABLE"]
        # The data and all elements are aligned appropriately for the hardware.
        assert self.matrix.flags["ALIGNED"]
        # This array is a copy of some other array.
        # spell-checker:words WRITEBACKIFCOPY
        assert not self.matrix.flags["WRITEBACKIFCOPY"]
