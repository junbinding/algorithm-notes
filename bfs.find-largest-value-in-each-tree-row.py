from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    515. 在每个树行中找最大值
    https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
    您需要在二叉树的每一行中找到最大的值。
    """
    # bfs
    class Solution:
        def largestValues(self, root: TreeNode) -> List[int]:
            res = []
            queue = [root]
            while queue and queue[0]:
                next = []
                tmp_max = queue[0].val
                for node in queue:
                    tmp_max = node.val if node.val > tmp_max else tmp_max

                    if node.left:
                        next.append(node.left)

                    if node.right:
                        next.append(node.right)
                res.append(tmp_max)
                queue = next

            return res






