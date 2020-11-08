from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    105. 从前序与中序遍历序列构造二叉树
    https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    根据一棵树的前序遍历与中序遍历构造二叉树。
    前序遍历 preorder = [3,9,20,15,7]，根 + 左 + 右
    中序遍历 inorder = [9,3,15,20,7]，左 + 根 + 右
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return

        # 找到根节点
        root = TreeNode(preorder[0])
        # 从中序列表中，通过根节点分割左右子树
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])

        return root


