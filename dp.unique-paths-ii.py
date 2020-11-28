from typing import List

class Solution:
    """
    63. 不同路径 II
    https://leetcode-cn.com/problems/unique-paths-ii/
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i == j == 0:
                        res[i][j] = 1
                    else:
                        a = res[i-1][j] if i != 0 else 0
                        b = res[i][j-1] if j != 0 else 0
                        res[i][j] = a + b

        return res[-1][-1]


so = Solution()
print(so.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
