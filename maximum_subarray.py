"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = -9999999
        max_to_here = 0

        for i in range(len(nums)):
            max_to_here = max_to_here + nums[i]
            if (current_max < max_to_here):
                current_max = max_to_here

            if max_to_here < 0:
                max_to_here = 0
        return current_max
"""
Runtime: 696 ms, faster than 97.28% of Python3 online submissions for Maximum Subarray.
Memory Usage: 27.9 MB, less than 55.60% of Python3 online submissions for Maximum Subarray.
"""