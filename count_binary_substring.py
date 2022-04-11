"""
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
"""
class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        consecutive_counts = []
        prev = 0
        curr = 0
        length = len(s)

        count = 0
        while (prev < length and curr < length):
            if s[prev] == s[curr]:
                count += 1
                curr += 1

            else:
                prev = curr
                consecutive_counts.append(count)
                count = 0

        consecutive_counts.append(count)
        res = 0

        for i in range(1, len(consecutive_counts)):
            res += min(consecutive_counts[i], consecutive_counts[i - 1])

        return res
"""
Success
Details
Runtime: 232 ms, faster than 54.89% of Python3 online submissions for Count Binary Substrings.
Memory Usage: 14.7 MB, less than 15.89% of Python3 online submissions for Count Binary Substrings.
Next challenges: 
"""