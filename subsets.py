"""
78. Subsets
Medium

9982

157

Add to List

Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result