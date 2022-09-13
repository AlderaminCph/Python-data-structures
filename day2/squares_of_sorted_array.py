"""
Given an integer array nums sorted
in non-decreasing order, return an
array of the squares of each number
sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Follow up: Squaring each element and sorting
the new array is very trivial, could you find
an O(n) solution using a different approach?
"""


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # two pointers: at the beginnig of array and at the end
        left = 0
        right = len(nums) - 1

        tracker = len(nums) - 1
        squared_array = [0 for i in nums]

        while tracker >= 0:
            if abs(nums(left)) >= abs(nums(right)):
                squared_array[tracker] = nums[left] ** 2
                left += 1
            else:
                squared_array[tracker] = nums[right] ** 2
                right -= 1
            tracker -= 1
        return squared_array
