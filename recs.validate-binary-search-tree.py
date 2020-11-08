# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    98. 验证二叉搜索树
    https://leetcode-cn.com/problems/validate-binary-search-tree/
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。
    假设一个二叉搜索树具有如下特征：
    - 节点的左子树只包含小于当前节点的数。
    - 节点的右子树只包含大于当前节点的数。
    - 所有左子树和右子树自身必须也是二叉搜索树。
    """
    pre = float('-inf')
    # 有效区间
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False

            if  not helper(node.left, lower, val):
                return False

            return True

        return helper(root, float('-inf'), float('inf'))


    # 中序
    def isValidBSTByInOrder(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if root.val <= self.pre:
            return False

        self.pre = root.val

        return self.isValidBST(root.right)





