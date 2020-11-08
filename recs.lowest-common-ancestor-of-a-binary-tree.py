# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    236. 二叉树的最近公共祖先
    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
    """
    # 递归
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right

        if not right:
            return left

        return root

        pass


