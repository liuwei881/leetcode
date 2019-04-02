# coding=utf-8

"""
Given two words word1 and word2, find the minimum number of steps required
to make word1 and word2 the same, where in each step you can delete one character
in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""


class Solution(object):
    def minDistance(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for x in range(len1 + 1)]
        for x in range(len1 + 1):
            for y in range(len2 + 1):
                if x == 0 or y == 0:
                    dp[x][y] = x + y
                elif word1[x - 1] == word2[y - 1]:
                    dp[x][y] = dp[x - 1][y - 1]
                else:
                    dp[x][y] = min(dp[x - 1][y], dp[x][y - 1]) + 1
        return dp[len1][len2]