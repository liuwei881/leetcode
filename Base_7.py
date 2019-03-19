# coding=utf-8

"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""

class Solution:
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        res = ''
        p = num > 0
        while num != 0:
            res = str(abs(num) % 7) + res
            num = int(abs(num) / 7)
        if p:
            return res
        return "-" + res


if __name__ == '__main__':
    a = Solution()
    num = -7
    print(a.convertToBase7(num))