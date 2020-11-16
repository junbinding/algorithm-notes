from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    102. 二叉树的层序遍历
    https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
    给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
    """
    # dfs
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(level, node):
            if not node:
                return

            if len(res) == level:
                res.append([])

            res[level].append(node.val)
            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)
        return res

    # bfs
    def levelOrderByBfs(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue

                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)

            if level:
                res.append(level)

        return res



