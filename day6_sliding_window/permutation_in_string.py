"""
567. Permutation in String

Given two strings s1 and s2,
return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one
of s1's permutations is the substring of s2.



Example 1:

>>> checkInclusion("ab","eidbaooo")
True

Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
>>> checkInclusion("ab","eidboaoo")
False

"""

import doctest


def checkInclusion(s1: str, s2: str) -> bool:
    """
    Solution Idea: sliding window and two hash maps
    """
    if len(s1) > len(s2):
        return False

    # two hash vectors with size of an alphabeth
    s1hash = [0] * 26
    s2hash = [0] * 26

    left = 0
    right = 0
    while right < len(s1):
        s1hash[ord(s1[right]) - ord("a")] += 1
        s2hash[ord(s2[right]) - ord("a")] += 1
        right += 1

    right -= 1  # to point right to the end of the window

    while right < len(s2):
        if s1hash == s2hash:
            return True
        right += 1
        if right != len(s2):
            s2hash[ord(s2[right]) - ord("a")] += 1
        s2hash[ord(s2[left]) - ord("a")] -= 1
        left += 1
    return False


doctest.testmod()
