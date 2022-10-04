"""
reverse the string, stack solution.

>>> reverse_string(["h","e","l","l","o"])
['o', 'l', 'l', 'e', 'h']

>>> reverse_string(["H","a","n","n","a","h"])
['h', 'a', 'n', 'n', 'a', 'H']
"""
from typing import List
import doctest


def reverse_string(s: List[str]):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    stack = []
    for char in s:
        stack.append(char)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1
    return s


doctest.testmod()
