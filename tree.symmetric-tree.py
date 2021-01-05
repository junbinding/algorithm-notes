# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    101. 对称二叉树
    https://leetcode-cn.com/problems/symmetric-tree/
    给定一个二叉树，检查它是否是镜像对称的。
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left or not right:
                return True

            if not (left and right):
                return False

            if left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)