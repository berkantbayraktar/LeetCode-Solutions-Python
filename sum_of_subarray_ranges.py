"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)

        for i in range(length):
            local_min = nums[i]
            local_max = nums[i]
            for j in range(i + 1, length):
                if nums[j] < local_min:
                    local_min = nums[j]
                elif nums[j] > local_max:
                    local_max = nums[j]
                res += local_max - local_min
        return res
"""
Success
Details
Runtime: 1636 ms, faster than 51.55% of Python3 online submissions for Sum of Subarray Ranges.
Memory Usage: 14.1 MB, less than 85.38% of Python3 online submissions for Sum of Subarray Ranges.
"""