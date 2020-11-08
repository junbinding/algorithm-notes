from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    144. 二叉树的前序遍历
    https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
    给定一个二叉树的根节点 root ，返回它的 前序 遍历。
    DLR--前序遍历（根在前，从左往右，一棵树的根永远在左子树前面，左子树又永远在右子树前面 ）
    LDR--中序遍历（根在中，从左往右，一棵树的左子树永远在根前面，根永远在右子树前面）
    LRD--后序遍历（根在后，从左往右，一棵树的左子树永远在右子树前面，右子树永远在根前面）
    """
    # 递归
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def pre_order(tree):
            if not tree:
                return None
            res.append(tree.val)
            pre_order(tree.left)
            pre_order(tree.right)

        pre_order(root)
        return res

    # 栈
    def preorderTraversalByStack(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.left, i.right, i.val])
            elif isinstance(i, int):
                res.append(i)

        return res


