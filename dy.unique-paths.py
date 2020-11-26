class Solution:
    """
    62. 不同路径
    https://leetcode-cn.com/problems/unique-paths/
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？
    """
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
                print('curr', i + 1, j + 1, cur[j-1], cur[j])
        return cur[-1]

    def uniquePathsByArr(self, m: int, n: int) -> int:
        # 生成缓存数组
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePathsByDy(self, m: int, n: int) -> int:
        if m == 1:
            return 1

        if n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


so = Solution()
print(so.uniquePaths(7, 3))
