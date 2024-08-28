#!/usr/bin/python3

"""
Module with island_perimeter function that returns
the perimeter of an island described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid
    """

    if not grid:
        return 0

    # determine number of rows and columns in grid & init perimeter to 0
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    # use nested loop to iterate through each cell in grid
    for r in range(rows):
        for c in range(cols):
            # check for each cell if it contains land
            if grid[r][c] == 1:
                # check all up, down, right, left for water
                # if water is found, increment perimeter by 1
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # check cells to the right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
