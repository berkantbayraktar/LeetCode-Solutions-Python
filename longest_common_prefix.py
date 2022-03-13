"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = min([len(el) for el in strs])
        longest_prefix = ''
        for iteration in range(max_length):
            current = ''
            for i in range(len(strs)):
                if i==0:
                    current = strs[i][iteration]
                else:
                    if strs[i][iteration] == current:
                        continue
                    else:
                        return longest_prefix
            longest_prefix += strs[0][iteration]
        return longest_prefix

"""
Success
Details 
Runtime: 41 ms, faster than 71.08% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 66.15% of Python3 online submissions for Longest Common Prefix.
"""