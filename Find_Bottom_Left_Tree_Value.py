# coding=utf-8

"""
Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
Input:
    2
   / \
  1   3
Output:
1
Example 2:
Input:
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        return self.findBottomLeftValue2(root, 1, [0, 0])

    def findBottomLeftValue2(self, root, depth, res):
        if res[1] < depth:
            res[0] = root
            res[1] = depth
        if root.left != None:
            findBottomLeftValue2(root.left, depth+1, res)
        if root.right != None:
            findBottomLeftValue2(root.right, depth+1, res)
        return res[0].val


if __name__ == '__main__':
    pass