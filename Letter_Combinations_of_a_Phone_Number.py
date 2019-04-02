# coding=utf-8

"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order,
your answer could be in any order you want.
"""


class Solution(object):
    def letterCombinations(self, digits):
        if digits == '':
            return []
        self.DigitDict = [' ', '1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = ['']
        for d in digits:
            res = self.letterCombBT(int(d), res)
        return res

    def letterCombBT(self, digit, oldStrList):
        return [dstr+i for i in self.DigitDict[digit] for dstr in oldStrList]