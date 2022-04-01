"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        pivot = length / 2 if length % 2 == 0 else (length - 1) / 2

        for i in range(length):
            if i < pivot:
                tmp = s[length - i - 1]
                s[length - i - 1] = s[i]
                s[i] = tmp
            else:
                break

"""
Success
Details
Runtime: 213 ms, faster than 79.72% of Python3 online submissions for Reverse String.
Memory Usage: 18.6 MB, less than 21.46% of Python3 online submissions for Reverse String.
"""