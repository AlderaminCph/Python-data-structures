"""
Given a string s,
reverse the order of characters in each word
within a sentence while still preserving
whitespace and initial word order.

Example 1:

>>> reverseWords("Lets take LeetCode contest")
'steL ekat edoCteeL tsetnoc'

Example 2:

>>> reverseWords("God Ding")
'doG gniD'

"""
import doctest


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()
    for i in range(len(words)):
        left = 0
        right = len(words[i]) - 1
        temp = list(words[i])
        while left < right:
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
        words[i] = "".join(temp)
    return (" ").join(words)


doctest.testmod()
