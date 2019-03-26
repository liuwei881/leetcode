# coding=utf-8

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often 
and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def kthSmallest(self, root, k):
		cnt = self.count(root.left)
		if k <= cnt:
			return self.kthSmallest(root.left, k)
		elif k > cnt + 1:
			return self.kthSmallest(root.right, k - cnt - 1)
		return root.val

	def count(self, node):
		if node == None:
			return 0
		return 1 + self.count(node.left) + self.count(node.right)