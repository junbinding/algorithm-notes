from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    """
    589. N叉树的前序遍历
    https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
    给定一个 N 叉树，返回其节点值的前序遍历。
    """
    def preorder(self, root: Node) -> List[int]:
        if not root:
            return []

        stack, res = [root], []
        while stack:
            root = stack.pop()

            if root:
                res.append(root.val)

            for c in root.children:
                stack.append(c)

        return res

    # 递归
    def preorderByRecursive(self, root: Node) -> List[int]:
        res = []
        def pre_order(node):
            if not node:
                return None

            res.append(node.val)
            for i in node.children:
                pre_order(i)


        pre_order(root)
        return res



