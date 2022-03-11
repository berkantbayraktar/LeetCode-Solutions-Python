# sliding window technique

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()  # traversed chars
        l = 0  # left pointer

        max_length = 0

        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[i])

            max_length = max(max_length, i - l + 1)

        return max_length