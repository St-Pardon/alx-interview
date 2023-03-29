#!/usr/bin/python3
'''island perimeter
'''

from collections import deque


def numofneighbour(grid, i, j):
    count = 0

    if (i > 0 and grid[i - 1][j]):
        count += 1

    if (j > 0 and grid[i][j - 1]):
        count += 1

    if (i < len(grid)-1 and grid[i + 1][j]):
        count += 1

    if (j < len(grid[0])-1 and grid[i][j + 1]):
        count += 1

    return count


def island_perimeter(grid):
    C = len(grid[0])
    R = len(grid)
    perimeter = 0

    for i in range(0, R):
        for j in range(0, C):
            if (grid[i][j]):
                perimeter += (4 - numofneighbour(grid, i, j))

    return perimeter
