from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    """
    590. N叉树的后序遍历
    https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
    给定一个 N 叉树，返回其节点值的后序遍历。
    """
    # 迭代
    def postorder(self, root: Node) -> List[int]:
        if not root:
            return []

        stack, res = [root], []
        while stack:
            root = stack.pop()

            if root:
                res.append(root.val)

            for c in root.children:
                stack.append(c)

            return res[::-1]


    # 递归
    def postorderByRecursive(self, root: Node) -> List[int]:
        res = []
        def post_order(node):
            if not node:
                return None

            for i in node.children:
                post_order(i)

            res.append(node.val)

        post_order(root)
        return res



