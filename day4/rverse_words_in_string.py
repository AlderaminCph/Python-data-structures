"""
Given a string s,
reverse the order of characters in each word
within a sentence while still preserving
whitespace and initial word order.

Example 1:

>>>reverseWords("Let's take LeetCode contest")
"s'teL ekat edoCteeL tsetnoc"

Example 2:

>>>reverseWords("God Ding")
"doG gniD"

"""
import doctest


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    res = []
    for word in s.split():
        left = 0
        right = len(word) - 1
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        res.append(word)
    return (" ").join(res)


doctest.testmod()
