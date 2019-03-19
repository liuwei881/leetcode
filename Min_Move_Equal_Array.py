# coding=utf-8

"""
Given a non-empty integer array, 
find the minimum number of moves required to make all array elements equal, 
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.
Example:
Input:
[1,2,3]
Output:
2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
[2,2,3]  =>  [2,2,2]

[2, 3, 4, 5] => [3, 3, 4, 5] => [3, 3, 3, 5] => [3, 3, 3, 4] => [3, 3, 3, 3]
"""


class Solution:
    def minMoves2(self, nums):
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0;
        while i < j:
            count += nums[j]-nums[i];
            i += 1
            j -= 1
        return count


if __name__ == '__main__':
    a = Solution()
    nums = [2, 3, 4, 5]
    print(a.minMoves2(nums))