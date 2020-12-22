# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    110. 平衡二叉树
    https://leetcode-cn.com/problems/balanced-binary-tree/
    给定一个二叉树，判断它是否是高度平衡的二叉树。
    本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
    """
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return abs(left - right) <= 1

    # 查询节点的最大深度
    def maxDepth(self, root):
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1