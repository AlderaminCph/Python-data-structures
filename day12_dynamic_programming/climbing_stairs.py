"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Example 1:

>>> s = Solution()
>>> s.climbStairs(2)
2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

>>> s.climbStairs(3)
3

Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
import doctest


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Dynamic programming
        Bottom up approach
        The result is the fibonnachi number of the stair length
        """
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


doctest.testmod()
