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


doctests.testmod()
