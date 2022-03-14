"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        traversed = set()

        for i in range(len(nums)):
            if nums[i] in traversed:
                return True
            else:
                traversed.add(nums[i])
        return False

"""
Success
Details
Runtime: 510 ms, faster than 70.74% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26 MB, less than 66.83% of Python3 online submissions for Contains Duplicate.
"""