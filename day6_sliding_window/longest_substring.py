"""
3. Longest Substring Without Repeating Characters
Given a string s,
find the length of the longest substring without repeating characters.



Example 1:

>>> lengthOfLongestSubstring("abcabcbb")
3

Explanation: The answer is "abc", with the length of 3.

Example 2:

>>> lengthOfLongestSubstring("bbbbb")
1

Explanation: The answer is "b", with the length of 1.

Example 3:

>>> lengthOfLongestSubstring("pwwkew")
3

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.


"""
import doctest


def lengthOfLongestSubstring(s):
    """
    Solution idea: slide window
    :type s: str
    :rtype: int
    """

    character_set = set()

    # two pointers to define a slide window
    left = 0
    result = 0
    for right in range(len(s)):
        # if there are a duplicates
        while s[right] in character_set:
            # update our window
            character_set.remove(s[left])
            left += 1  # update left pointer
        character_set.add(s[right])
        result = max(result, right - left + 1)
    return result


doctest.testmod()
