"""
162. Find Peak Element
Medium

6047

3734

Add to List

Share
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
"""

import sys

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        minInt = -sys.maxsize
        nums = [minInt] + nums + [minInt]
        
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i - 1