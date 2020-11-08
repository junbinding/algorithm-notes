from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    """
    429. N叉树的层序遍历
    https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
    给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
    """
    # 迭代
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []

        next_level, res = [root], []
        i = 0
        while len(next_level) > 0:
            tmp_next = []
            if next_level:
                res.append([])

            for c in next_level:
                res[i].append(c.val)
                if not c.children: continue
                tmp_next.extend(c.children)

            next_level = tmp_next
            i += 1

        return res

