# coding=utf-8

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        maps = {}
        maps2 = {}
        for i in s:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1
        for j in t:
            if j in maps2:
                maps2[j] += 1
            else:
                maps2[j] = 1
        if maps == maps2:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    print(a.isAnagram('anagram', 'nagaram'))
