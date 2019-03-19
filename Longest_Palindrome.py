# coding=utf-8
"""
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
1、统计所有字母的出现频率（分大小写） 
2、统计只出现奇数次数字母的个数 
3、如果2中结果不为0，字符串的长度减去2中的字母个数+1
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        maps = {}
        b = 0
        for i in s:
            if i not in maps:
                maps[i] = 1
            else:
                maps[i] += 1
        for v in maps.values():
            if int(v % 2) != 0:
                b+=1
        if b != 0:
            return len(s) - b + 1
        return len(s)


if __name__ == '__main__':
    a = Solution()
    s = "level"
    print(a.longestPalindrome(s))