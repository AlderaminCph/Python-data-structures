"""
Given a string s, you can transform every letter individually to be lowercase
or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in
any order.

Example 1:
>>> s = Solution()
>>> s.letterCasePermutation("a1b2")
['a1b2', 'a1B2', 'A1b2', 'A1B2']

Example 2:
>>> s.letterCasePermutation("3z4")
['3z4', '3Z4']

"""
from typing import List
import doctest


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]

        for char in s:
            tmp = []
            if char.isalpha():
                for item in output:
                    tmp.append(item + char.lower())
                    tmp.append(item + char.upper())
            else:
                for item in output:
                    tmp.append(item + char)
            output = tmp

        return output


doctest.testmod()
