"""
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

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
from collections import defaultdict
import doctest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for item in nums:
            d[item] += 1
        return list(d.keys())[list(d.values()).index(1)]


doctest.testmod()
