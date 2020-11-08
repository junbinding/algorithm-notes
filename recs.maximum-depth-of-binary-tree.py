class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    104. 二叉树的最大深度
    https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
    给定一个二叉树，找出其最大深度。
    二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
    说明: 叶子节点是指没有子节点的节点。
    """
    # 递归
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right))+ 1

    # 迭代
    def maxDepthByIteration(self, root: TreeNode) -> int:
        if not root:
            return 0

        rest = [root]
        level = 1
        while rest:
            tmp_rest = []
            for i in rest:
                if i.left:
                    tmp_rest.append(i.left)
                if i.right:
                    tmp_rest.append(i.right)

            rest = tmp_rest
            if tmp_rest:
                level += 1

        return level