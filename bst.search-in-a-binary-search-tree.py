# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    700. 二叉搜索树中的搜索
    https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
    给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
    """
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val:
            return self.searchBST(root.right, val)

        return root


