"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either
 index i or index i + 1 on the next row.



Example 1:
>>> Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
11

Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11
(underlined above).

Example 2:

>>> Solution().minimumTotal([[-10]])
-10
"""
from typing import List
import doctest


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        bottom_row = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for ind, value in enumerate(row):
                bottom_row[ind] = value + min(
                    bottom_row[ind], bottom_row[ind + 1]
                )
        return bottom_row[0]


doctest.testmod()
