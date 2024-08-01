#!/usr/bin/python3
"""
Module to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A 2D grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check each side of the cell
                if i == 0 or grid[i - 1][j] == 0:  # Check top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Check bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
