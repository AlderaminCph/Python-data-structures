"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each
cell.

The distance between two adjacent cells is 1.

Example 1:
>>> updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
[[0,0,0],[0,1,0],[0,0,0]]

>>> updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
[[0,0,0],[0,1,0],[1,2,1]]
"""
import doctests
from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    """
    Solution
    """
    height = len(mat)
    width = len(mat[0])
    q = []

    for i in range(height):
        for j in range(width):
            if mat[i][j] == 0:
                q.append((i, j))
            else:
                mat[i][j] = "#"

    for row, column in q:
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr = row + dx
            nc = column + dy

            if 0 <= nr <= height and 0 <= nc <= width and mat[nr][nc] == "#":
                mat[nr][nc] = mat[row][column] + 1
                q.append((nr, nc))
    return mat


doctests.testmod()
