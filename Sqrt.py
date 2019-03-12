# coding=utf-8

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer,
the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left < right:
            mid = int(left + (right - left) / 2)
            if mid > x / mid:
                right = mid - 1
            elif mid == x / mid:
                return int(mid)
            else:
                if mid + 1 > x / (mid + 1):
                    return int(mid)
                if mid + 1 == x / (mid + 1):
                    return int(mid + 1)
                left = mid + 1
        return int((left + right) / 2)


if __name__ == '__main__':
    a = Solution()
    print(a.mySqrt(7))