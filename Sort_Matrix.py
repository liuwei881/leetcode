# coding=utf-8

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

class Solution:
    def kthSmallest(self, matrix, k):
        l = []
        for i in matrix:
            l.extend(i)
        l.sort()
        return l[k-1]

if __name__ == '__main__':
    a = Solution()
    matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
    print(a.kthSmallest(matrix, 8))