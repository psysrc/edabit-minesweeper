import numpy as np


_mine_char = "#"
_empty_char = "-"
_accepted_chars = [_empty_char, _mine_char]


def _validate_grid(grid: np.array):
    for value in np.nditer(grid):
        if value not in _accepted_chars:
            raise ValueError(f"Cannot generate minesweeper grid (invalid cell value '{value}')")


def _set_empty_to_zero(grid: np.array):
    """Changes all cells containing '_empty_char' with '0'."""
    for index, value in np.ndenumerate(grid):
        if value == _empty_char:
            grid[index] = "0"


def _is_valid_index(index: tuple, grid: np.array) -> bool:
    """Returns whether or not the 'index' is valid for the provided 'grid'."""
    if index[0] < 0 or index[0] >= grid.shape[0]:
        return False
    
    if index[1] < 0 or index[1] >= grid.shape[1]:
        return False
    
    return True


def _gen_surrounding_indices(index: tuple, grid: np.array) -> set:
    """Returns all surrounding indices of a given 'index' on the 'grid'."""
    indices = set()

    for hor_offset in [-1, 0, 1]:
        for ver_offset in [-1, 0, 1]:
            new_index = (index[0] + ver_offset, index[1] + hor_offset)

            if new_index != index:
                if _is_valid_index(new_index, grid):
                    indices.add(new_index)

    return indices


def _increment_surrounding_cells(grid: np.array, index: tuple):
    """Takes an 'index' in the 'grid' and increments the value of all surrounding cells by one."""
    for surrounding_index in _gen_surrounding_indices(index, grid):
        value = grid[surrounding_index]

        if value != _mine_char:
            new_value = int(value) + 1
            grid[surrounding_index] = new_value


def _calculate_cell_values(grid: np.array):
    for index, value in np.ndenumerate(grid):
        if value == _mine_char:
            _increment_surrounding_cells(grid, index)


def gen_grid(grid: np.array):
    if type(grid) != np.array:
        grid = np.array(grid)
    
    _validate_grid(grid)

    output_grid = grid.copy()
    _set_empty_to_zero(output_grid)

    _calculate_cell_values(output_grid)

    return output_grid


def main():
    my_grid = np.array([
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ])

    my_generated_grid = gen_grid(my_grid)

    print(my_grid)
    print()
    print(my_generated_grid)


if __name__ == "__main__":
    main()
