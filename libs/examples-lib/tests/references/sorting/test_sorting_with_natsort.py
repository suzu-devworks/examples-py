"""This test is for learning to sort using natural sorting like Windows.

References:
    - https://github.com/SethMMorton/natsort

"""

import os

from natsort import natsorted, ns, os_sorted, realsorted


def test_natural_sorting() -> None:
    # fmt: off
    list1 = [
        "2 ft 7 in",
        "1 ft 5 in",
        "10 ft 2 in",
        "2 ft 11 in",
        "7 ft 6 in",
        ]
    # fmt: om

    # use normal sorted
    sorted_result = sorted(list1)
    assert sorted_result == [
        "1 ft 5 in",
        "10 ft 2 in",
        "2 ft 11 in",
        "2 ft 7 in",
        "7 ft 6 in",
        ]

    # use natsorted
    natural_result = natsorted(list1)
    assert natural_result == [
        "1 ft 5 in",
        "2 ft 7 in",
        "2 ft 11 in",
        "7 ft 6 in",
        "10 ft 2 in",
    ]

    # version number sort
    # fmt: off
    list2 = [
        "version-1.9",
        "version-2.0",
        "version-1.11",
        "version-1.10",
        ]
    # fmt: on
    natural_result = natsorted(list2)
    assert natural_result == [
        "version-1.9",
        "version-1.10",
        "version-1.11",
        "version-2.0",
    ]


def test_natural_real_sorting() -> None:
    """Real(signed float values) sorting."""

    #                +5.10                 -3.00             +5.30               +2.00
    list1 = [
        "position5.10.data",
        "position-3.data",
        "position5.3.data",
        "position2.data",
    ]

    # use natsorted
    natural_result = natsorted(list1)
    assert natural_result == [
        "position2.data",
        "position5.3.data",
        "position5.10.data",
        "position-3.data",
    ]

    # use natsorted with REAL parameter
    real_result = natsorted(list1, alg=ns.REAL)
    assert real_result == [
        "position-3.data",
        "position2.data",
        "position5.10.data",
        "position5.3.data",
    ]

    # use realsorted, shortcut for natsorted with alg=ns.REAL
    real_result = realsorted(list1)
    assert real_result == [
        "position-3.data",
        "position2.data",
        "position5.10.data",
        "position5.3.data",
    ]


def test_natural_windows_sorting() -> None:
    """Return value that will be different depending on your platform."""

    dirs = os.listdir(".")
    _ = os_sorted(dirs)
    pass
