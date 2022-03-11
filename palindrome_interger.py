'''
Q- 
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_str_reversed = x_str[::-1]
        
        return x_str == x_str_reversed