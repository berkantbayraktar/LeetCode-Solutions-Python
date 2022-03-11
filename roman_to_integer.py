"""
Q - Given a roman numeral, convert it to an integer.
Example 1:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        symbol_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        for i in range(len(s)):
            if i+1 < len(s) and symbol_dict[s[i+1]] > symbol_dict[s[i]]:
                result -= symbol_dict[s[i]]
            else:
                result += symbol_dict[s[i]]
        return result
        

'''
Runtime: 41 ms, faster than 95.45% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 54.53% of Python3 online submissions for Roman to Integer.
'''