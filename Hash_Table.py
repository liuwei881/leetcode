# coding=utf-8

"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    """
    numbers: inputs sorted list
    target: int

    Example:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    """
    def twoSum(self, numbers, target):
        map = {}
        for i in range(len(numbers)):
            if numbers[i] not in map:
                map[target - numbers[i]] = i
            else:
                return map[numbers[i]], i


if __name__ == '__main__':
    # numbers = [2, 3, 4]
    # target = 6
    numbers = [2, 7, 11, 15]
    target = 9
    a = Solution()
    print(a.twoSum(numbers, target))