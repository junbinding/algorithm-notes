from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    111. 二叉树的最小深度
    https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
    给定一个二叉树，找出其最小深度。
    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    说明：叶子节点是指没有子节点的节点。
    """
    # 广度优先
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        return 0


    # 递归
    def minDepthByRecursive(self, root: TreeNode) -> int:
        if not root:
            return 0

        m1 = self.minDepth(root.left)
        m2 = self.minDepth(root.right)

        if not root.left or not root.right:
            return m1 + m2 + 1

        return min(self.minDepth(root.left), self.minDepth(root.right))+ 1
