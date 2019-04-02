# coding=utf-8

"""
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
"""
class Solution {
public:
    int numSquares(int n) {
        while (n % 4 == 0) n /= 4;
        if (n % 8 == 7) return 4;
        for (int a = 0; a * a <= n; ++a) {
            int b = sqrt(n - a * a);
            if (a * a + b * b == n) {
                return !!a + !!b;
            }
        }
        return 3;
    }
};
"""


# class Solution:
#     def numSquares(self, n):
#         distance = [0 for _ in range(n+1)]
#
#         for i in range(1, n+1):
#             count = square = 1
#             min_distance = n
#             while square <= i:
#                 check_distance = 1 + distance[i-square]
#                 if check_distance < min_distance:
#                     min_distance = check_distance
#                 count += 1
#                 square = count * count
#             distance[i] = min_distance
#
#         return distance[n]


class Solution:
    def numSquares(self, n):
        k = n
        while k % 4 == 0:
            k = k // 4
        if k % 8 == 7:
            return 4
        i = 0
        while i ** 2 <= n:
            j = 0
            while j ** 2 <= n-(i**2):
                if i ** 2 + j ** 2 == n:
                    return (1 if i > 0 else 0) + (1 if j > 0 else 0)
                j += 1
            i += 1
        return 3


if __name__ == '__main__':
    a = Solution()
    print(a.numSquares(12))
