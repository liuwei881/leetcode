# coding=utf-8

# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution
# and you may not use the same element twice.


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
                return map[numbers[i]]+1, i+1


if __name__ == '__main__':
    # numbers = [2, 7, 11, 15]
    # target = 9
    numbers = [2, 3, 4]
    target = 6
    # numbers = [5, 25, 75]
    # target = 100
    a = Solution()
    print(a.twoSum(numbers, target))
