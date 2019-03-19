# coding=utf-8

"""
Given an array of numbers nums, 
in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant space complexity?
"""

class Solution:
    def singleNumber(self, nums):
        maps = {}
        for i in nums:
            if i not in maps:
                maps[i] = 1
            else:
                maps[i] += 1
        m = [k for k, v in maps.items() if v == 1]
        return m


#class Solution:
#    def singleNumber(self, nums):
#        xor = nums[0]
#        for i in range(len(nums)):
#            xor ^= nums[i]
#        return xor


if __name__ == '__main__':
    a = Solution()
    nums = [1,2,1,3,2,5]
    print(a.singleNumber(nums))
