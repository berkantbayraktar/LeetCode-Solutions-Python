"""
796. Rotate String
Easy

1846

86

Add to List

Share
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            new_s = s[i+1:] + s[:i+1]
            if new_s == goal:
                return True
        return False