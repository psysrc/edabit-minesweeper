import pytest
from minesweeper.minesweeper import gen_grid
import numpy as np


def test_basic1():
    generated_grid = gen_grid([
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ])
    
    expected_grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "1", "#", "1", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    assert np.array_equal(generated_grid, expected_grid)


def test_basic2():
    generated_grid = gen_grid([
        ["-", "-", "-", "-", "#"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["#", "-", "-", "-", "-"],
    ])
    
    expected_grid = [
        ["0", "0", "0", "1", "#"],
        ["0", "1", "1", "2", "1"],
        ["0", "1", "#", "1", "0"],
        ["1", "2", "1", "1", "0"],
        ["#", "1", "0", "0", "0"],
    ]

    assert np.array_equal(generated_grid, expected_grid)


def test_basic3():
    generated_grid = gen_grid([
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ])
    
    expected_grid = [
        ["1", "1", "2", "#", "#"],
        ["1", "#", "3", "3", "2"],
        ["2", "4", "#", "2", "0"],
        ["1", "#", "#", "2", "0"],
        ["1", "2", "2", "1", "0"],
    ]

    assert np.array_equal(generated_grid, expected_grid)


def test_warzone():
    generated_grid = gen_grid([
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
    ])
    
    expected_grid = [
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
    ]

    assert np.array_equal(generated_grid, expected_grid)


def test_dmz():
    generated_grid = gen_grid([
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ])
    
    expected_grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    assert np.array_equal(generated_grid, expected_grid)


def test_error_bad_cell_value1():
    with pytest.raises(ValueError):
        gen_grid([
            ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "=", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"],
        ])


def test_error_bad_cell_value2():
    with pytest.raises(ValueError):
        gen_grid([
            ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", 0, "#", "-", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"],
        ])


def test_error_bad_cell_value3():
    with pytest.raises(ValueError):
        gen_grid([
            ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "=", "-"],
            ["-", "#", "", "-", "-"],
            ["-", "-", "-", "-", "-"],
        ])


def test_error_bad_cell_value4():
    with pytest.raises(ValueError):
        gen_grid([
            ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "##", "=", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"],
        ])
