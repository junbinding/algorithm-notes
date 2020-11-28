from typing import List


class Solution:
    """
    120. 三角形最小路径和
    https://leetcode-cn.com/problems/triangle
    给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
    相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]

    # dfs
    def minimumTotalByDfs(self, triangle: List[List[int]]) -> int:
        def dfs(l, i, j):
            if len(l) == i:
                return 0

            return min(dfs(l, i + 1, j), dfs(l, i + 1, j + 1)) + l[i][j]
        return dfs(triangle, 0, 0)

    # 递推
    def minimumTotalByDp(self, triangle: List[List[int]]) -> int:
        # 定义状态数组
        l = len(triangle)
        # 为了防止数组越界，会比原数组多申请一行列的空间
        dp = [[0] * (l + 1) for _ in range(l + 1) ]
        for i in range(len(triangle) - 1, -1, -1):
            for j in range(0, len(triangle[i])):
                # 定义状态方程 d[i][j] = 下一行的同列节点 + 下一行的下一列节点 + 当前行列的值
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]


so = Solution()
print(so.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
