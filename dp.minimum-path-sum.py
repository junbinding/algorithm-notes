from typing import List


class Solution:
    """
    64. 最小路径和
    https://leetcode-cn.com/problems/minimum-path-sum/
    给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        l = len(grid)
        if l == 0:
            return 0

        m = len(grid[0])
        if m == 0:
            return 0

        dp = [[0] * m for _ in range(l)]
        dp[0][0] = grid[0][0]

        for i in range(l):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

so = Solution()
print(so.minPathSum([[1,2,3],[4,5,6]]))
