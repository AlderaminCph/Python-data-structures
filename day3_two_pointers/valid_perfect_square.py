"""
Given a positive integer num, write a function which returns
True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true

Example 2:

Input: num = 14
Output: false

"""


def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    left = 1
    right = num
    if num == 1:
        return True
    while left < right:
        mid = int(left + (right - left) / 2)
        print("mid", mid)
        sq_mid = mid * mid
        print("sq_mid", sq_mid)
        if sq_mid == num:
            return True
        elif sq_mid > num:
            right = mid
        else:
            left = mid + 1
    return False
