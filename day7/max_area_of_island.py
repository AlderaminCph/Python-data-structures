"""
695. Max Area of Island

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

>>> maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]])
6

Explanation: The answer is not 11,
because the island must be connected 4-directionally.

Example 2:

>>> maxAreaOfIsland([0,0,0,0,0,0,0,0]])
Output: 0

"""

import doctest
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """
    Solution idea: depth first search (DFS)
    """
    rows, cols = len(grid), len(grid[0])
    visit = set()  # visit hash set

    def dfs(row: int, col: int) -> int:
        """
        Performs depth first search to calculates
        the area of an island
        :return area of an island
        """
        # if we got out of bounds
        if (
            row < 0
            or row == row
            or col < 0
            or col == cols
            or grid[row][col] == 0
            or (row, col) in visit
        ):
            return 0
        visit.add((row, col))
        return (
            1
            + dfs(row + 1, col)
            + +dfs(row - 1, col)
            + +dfs(row, col + 1)
            + +dfs(row, col - 1)
        )

    max_area = 0
    for row in range(rows):
        for col in range(cols):
            max_area = max(max_area, dfs(row, col))
    return max_area


doctest.testmod()
