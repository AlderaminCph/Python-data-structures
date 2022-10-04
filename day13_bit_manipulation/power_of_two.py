"""Given an integer n, return true if it is a power of two. Otherwise,
return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:
>>> Solution().isPowerOfTwo(1)
True

Explanation: 20 = 1

Example 2:
>>> Solution().isPowerOfTwo(16)
True

Explanation: 24 = 16

Example 3:
>>> Solution().isPowerOfTwo(3)
False
"""
import doctest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        value = n
        while value % 2 == 0:
            value = value / 2
        if value == 1:
            return True
        return False


doctest.testmod()
