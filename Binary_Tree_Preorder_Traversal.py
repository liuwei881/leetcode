# coding=utf-8

"""
Given a binary tree, return the preorder traversal of its nodes' values.
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    result = []
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        seq = []
        while ((root != None) or (len(stack) != 0)):
            if root != None:
                seq.append(root.val)
                stack.append(root)  
                root = root.left   
            else:
                root = stack.pop()
                root = root.right
        return seq


if __name__ == '__main__':
    root = TreeNode(1)
    root = TreeNode(2)
    root = TreeNode(3)
    a = Solution()
    print(a.preorderTraversal(root))