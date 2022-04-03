from minesweeper.minesweeper import _is_valid_index, _gen_surrounding_indices
import numpy as np


def test_is_valid_index():
    grid = np.array([
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ])

    # Valid
    assert _is_valid_index((0, 0), grid)
    assert _is_valid_index((0, 4), grid)
    assert _is_valid_index((2, 0), grid)
    assert _is_valid_index((2, 4), grid)

    # Invalid (negative)
    assert not _is_valid_index((-1, 0), grid)
    assert not _is_valid_index((0, -1), grid)
    assert not _is_valid_index((-1, -1), grid)

    # Invalid (crazy negative)
    assert not _is_valid_index((-54, 0), grid)
    assert not _is_valid_index((0, -24528384), grid)
    assert not _is_valid_index((-3285524, -927862), grid)

    # Invalid (out of bounds)
    assert not _is_valid_index((3, 0), grid)
    assert not _is_valid_index((0, 5), grid)
    assert not _is_valid_index((3, 5), grid)

    # Invalid (crazy out of bounds)
    assert not _is_valid_index((92725, 0), grid)
    assert not _is_valid_index((0, 108768), grid)
    assert not _is_valid_index((24987, 262436534), grid)


def test_gen_surrounding_indices1():
    grid = np.array([
        ["#", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ])

    index = (0, 0)
    indices = _gen_surrounding_indices(index, grid)

    assert index not in indices

    assert (0, 1) in indices
    assert (1, 0) in indices
    assert (1, 1) in indices

    assert (-1, -1) not in indices
    assert (-1, 0) not in indices
    assert (-1, 1) not in indices
    assert (0, -1) not in indices
    assert (-1, -1) not in indices

    assert len(indices) == 3


def test_gen_surrounding_indices2():
    grid = np.array([
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "#"],
    ])

    index = (2, 4)
    indices = _gen_surrounding_indices(index, grid)

    assert index not in indices

    assert (1, 3) in indices
    assert (1, 4) in indices
    assert (2, 3) in indices

    assert (1, 5) not in indices
    assert (2, 5) not in indices
    assert (3, 3) not in indices
    assert (3, 4) not in indices
    assert (3, 5) not in indices

    assert len(indices) == 3

def test_gen_surrounding_indices3():
    grid = np.array([
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ])

    index = (1, 2)
    indices = _gen_surrounding_indices(index, grid)

    assert index not in indices

    assert (0, 1) in indices
    assert (0, 2) in indices
    assert (0, 3) in indices
    assert (1, 1) in indices
    assert (1, 3) in indices
    assert (2, 1) in indices
    assert (2, 2) in indices
    assert (2, 3) in indices

    assert len(indices) == 8
