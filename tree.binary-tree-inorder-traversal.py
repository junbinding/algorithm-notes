from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    94. 二叉树的中序遍历
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
    给定一个二叉树的根节点 root ，返回它的 中序 遍历。
    DLR--前序遍历（根在前，从左往右，一棵树的根永远在左子树前面，左子树又永远在右子树前面 ）
    LDR--中序遍历（根在中，从左往右，一棵树的左子树永远在根前面，根永远在右子树前面）
    LRD--后序遍历（根在后，从左往右，一棵树的左子树永远在右子树前面，右子树永远在根前面）
    """
    # 递归
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def in_order(tree):
            if not tree:
                return None
            in_order(tree.left)
            res.append(tree.val)
            in_order(tree.right)

        in_order(root)
        return res

    # 栈
    def inorderTraversalByStack(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                res.append(i)

        return res


