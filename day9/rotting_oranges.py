"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange. If this is impossible, return -1.

>>> orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
4

Example 2:

>>> orangesRotting([2,1,1],[0,1,1],[1,0,1]])
-1
Explanation: The orange in the bottom left corner (row 2, column 0) is never
rotten, because rotting only happens 4-directionally.

Example 3:

>>> orangesRotting([[0,2]])
0
Explanation: Since there are already no fresh oranges at minute 0, the answer
is just 0.

"""
from typing import List
from collections import deque
import doctest


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Solution
        """
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:  # count the number of fresh oranges
                    fresh += 1
                if grid[r][c] == 2:  # add every rotting orange to the queue
                    q.append([r, c])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()  # dlete rotting orange from queue
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    # if in bounds and fresh, make rotten
                    if (
                        row < 0
                        or row == ROWS
                        or col < 0
                        or col == COLS
                        or grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] == 2  # make orange rotten
                    fresh -= 1  # decrement the number of fresh oranges
                    q.append([row][col])
            time += 1
        return time if fresh == 0 else -1


doctest.testmod()
