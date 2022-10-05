"""
O(1) memory solution vith XOR for the single number problem

Example 1:

>>> Solution().singleNumber([2,2,1])
1

Example 2:

>>> Solution().singleNumber([4,1,2,1,2])
4

Example 3:

>>> Solution().singleNumber([1])
1
"""
from typing import List
import doctest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # n ^ 0 = n
        for n in nums:
            res = n ^ res
        return res


doctest.testmod()
