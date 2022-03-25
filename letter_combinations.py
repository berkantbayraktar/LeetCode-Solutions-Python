import itertools
"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combs = []
        ret = []
        number_dict = {"2": ["a", "b", "c"],
                       "3": ["d", "e", "f"],
                       "4": ["g", "h", "i"],
                       "5": ["j", "k", "l"],
                       "6": ["m", "n", "o"],
                       "7": ["p", "q", "r", "s"],
                       "8": ["t", "u", "v"],
                       "9": ["w", "x", "y", "z"]}

        combinations = [''] if digits else []
        for digit in digits:
            combinations = [comb + letter for comb in combinations for letter in number_dict[digit]]
        return combinations

"""
Success
Details
Runtime: 46 ms, faster than 46.53% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 38.48% of Python3 online submissions for Letter Combinations of a Phone Number.
"""