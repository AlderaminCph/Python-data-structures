"""
Given two integer arrays arr1 and arr2, and the integer d,
 return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i]
 such that there is not any element
 arr2[j] where |arr1[i]-arr2[j]| <= d.



Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2

Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1

"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums) - 1

    # Traverse the search space
    while start <= end:

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    # Return the insert position
    return end + 1


def findTheDistanceValue(arr1, arr2, d):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type d: int
    :rtype: int
    """
    ans = 0
    arr2.sort()
    last = len(arr2)
    for el in arr1:
        index = searchInsert(arr2, el)  # left index
        min_dist = float("inf")  # initialize to a very huge number
        if index > 0:
            min_dist = min(min_dist, abs(el - arr2[index - 1]))
        if index < last:
            min_dist = min(min_dist, abs(el - arr2[index]))
        if min_dist > d:
            ans += 1
    return ans
