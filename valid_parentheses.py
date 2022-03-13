"""
Q- 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 2:

Input: s = "()[]{}"
Output: true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = list()
        bracket_dict = {'(' : ')',
                       '{' : '}',
                       '[' : ']'}
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                my_stack.append(s[i])
            else:
                if len(my_stack) > 0  and bracket_dict[my_stack.pop()] == s[i]:
                    continue
                else:
                    return False
        return len(my_stack) == 0

"""
Success
Details 
Runtime: 38 ms, faster than 69.17% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 82.06% of Python3 online submissions for Valid Parentheses.
"""

