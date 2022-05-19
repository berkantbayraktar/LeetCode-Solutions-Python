"""
384. Shuffle an Array
Medium

782

665

Add to List

Share
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
"""

import random

class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        length = len(self.nums)
        new_arr = []
        for i in range(length):
            rand_int = random.randint(0, length-1-i)
            new_arr.append(self.nums.pop(rand_int))
        self.nums = new_arr
        return new_arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()