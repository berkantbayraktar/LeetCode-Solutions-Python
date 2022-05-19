"""
164. Maximum Gap
Hard

2101

286

Add to List

Share
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.
"""

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_diff = 0
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > max_diff:
                max_diff = nums[i] - nums[i-1]
        
        return max_diff