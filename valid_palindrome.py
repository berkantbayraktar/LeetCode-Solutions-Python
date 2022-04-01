'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = ''

        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z':
                filtered_str += str.lower(s[i])
            elif 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
                filtered_str += s[i]

        return filtered_str[::-1] == filtered_str

'''
Success
Details
Runtime: 58 ms, faster than 68.21% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.6 MB, less than 47.58% of Python3 online submissions for Valid Palindrome.
'''