"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        nums1_l = len(nums1)
        nums2_l = len(nums2)

        for i in range(nums1_l + nums2_l):
            ptr = 0
            if nums1 and nums2:
                if nums1[ptr] < nums2[ptr]:
                    el = nums1.pop(0)
                    merged_list.append(el)
                else:
                    el = nums2.pop(0)
                    merged_list.append(el)
            elif nums1:
                el = nums1.pop(0)
                merged_list.append(el)
            elif nums2:
                el = nums2.pop(0)
                merged_list.append(el)

        t_length = nums1_l + nums2_l

        if t_length % 2 == 0:
            t_length = floor((t_length) / 2)
            return (merged_list[t_length] + merged_list[t_length - 1]) / 2
        else:
            t_length = floor(t_length / 2)
            return merged_list[t_length]


"""
Success
Details
Runtime: 104 ms, faster than 78.15% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 78.53% of Python3 online submissions for Median of Two Sorted Arrays.
"""