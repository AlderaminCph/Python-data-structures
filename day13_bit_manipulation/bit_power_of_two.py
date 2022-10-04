"""
Bit manipulation to solve the power of two problem

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
        if n <= 0:
            return False
        return n & (n - 1) == 0


doctest.testmod()
