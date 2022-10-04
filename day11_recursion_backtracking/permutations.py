"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:

>>> s = Solution()
>>> s.permute([1,2,3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Example 2:

>>> s.permute([0,1])
[[0, 1], [1, 0]]

Example 3:

>>> s.permute([1])
[[1]]

"""
import doctest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # basecase
        if len(nums) == 1:
            return [nums.copy()]

        for item in nums:
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result


doctest.testmod()
