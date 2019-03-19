# coding=utf-8

"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        maps = {}
        for i in nums:
            if i not in maps:
                maps[i] = 1
            else:
                maps[i] += 1
        n = int(len(nums) / 2)
        return sorted(maps.items(), key=lambda item:item[1], reverse=True)[0][0]


if __name__ == '__main__':
    a = Solution()
    nums = [6, 5, 5]
    print(a.majorityElement(nums))