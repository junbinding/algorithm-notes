# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    450. 删除二叉搜索树中的节点
    https://leetcode-cn.com/problems/delete-node-in-a-bst/
    https://www.geekxh.com/1.4.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%B3%BB%E5%88%97/405.html#_04%E3%80%81go%E8%AF%AD%E8%A8%80%E7%A4%BA%E4%BE%8B
    给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
    一般来说，删除节点可分为两个步骤：
    - 首先找到需要删除的节点；
    - 如果找到了，删除它。
    - 说明：要求算法时间复杂度为 O(h)，h 为树的高度。
    """
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # 当走到这里的时候，代表已经找到 root
        # 如果右子树为空，则用左子树代替自己
        if not root.right:
            return root.left

        # 如果左子树为空，则用右子树代替自己
        if not root.left:
            return root.right

        # 如果左右子树都不为空，则找到比当前节点大的右侧最小节点
        min_node = root.right

        while min_node.left:
            min_node = min_node.left

        root.val = min_node.val
        # 右侧节点需要删除最小的元素
        root.right = self.deleteMinNode(root.right)
        return root

    # 删除最小节点
    def deleteMinNode(self, root):
        # 如果当前节点没有左子节点，则直接返回右子节点
        if not root.left:
            p_right = root.right
            root.right = None
            return p_right

        # 删除左侧的最小子节点
        root.left = self.deleteMinNode(root.left)
        return root
