"""
Given an array, rotate the array to the right
by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Follow up:

    Try to come up with as many solutions as you can.
    There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""


def gcd(a, b):
    """
    Function to get gcd of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def rotate(nums, k):
    """
    Solution (A Juggling Algorithm): divide the array
    in different sets where number of sets
    is equal to GCD of len(nums)
    and k and move the elements within sets.
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for i in range(gcd(k, len(nums))):
        # move i-th values of blocks
        n = len(nums)
        temp = nums[(n - 1) - i]
        j = i
        while True:
            d = j + k
            if d >= len(nums):
                d = d - len(nums)
            if d == i:
                break
            nums[(n - 1) - j] = nums[(n - 1) - d]
            j = d
        nums[(n - 1) - j] = temp
