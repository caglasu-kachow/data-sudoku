# pylint: disable=missing-docstring




def _is_valid_group(group: list[int]) -> bool:
    """1 to 9 once each"""
    return sorted(group) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sudoku_validator(grid: list[list[int]]) -> bool:
    # Rows
    for row in grid:
        if not _is_valid_group(row):
            return False

    # Columns
    for col_idx in range(9):
        col = [grid[row_idx][col_idx] for row_idx in range(9)]
        if not _is_valid_group(col):
            return False

    # 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    box.append(grid[r][c])
            if not _is_valid_group(box):
                return False

    return True
