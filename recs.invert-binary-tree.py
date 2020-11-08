# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    226. 翻转二叉树
    https://leetcode-cn.com/problems/invert-binary-tree/
    翻转一棵二叉树。
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert_tree(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            invert_tree(node.left)
            invert_tree(node.right)

        invert_tree(root)
        return root

