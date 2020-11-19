from typing import List

class Solution:
    """
    200. 岛屿数量
    https://leetcode-cn.com/problems/number-of-islands/
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
    """
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        # 遍历上下左右四个点
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            # 如果没有超出网格，且仍旧是岛屿，则也将置位水滴
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    # 通过不断将岛屿相连的陆地置为水滴来计算独立岛屿个数
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        # 遍历循环每个元素
        for r in range(nr):
            for c in range(nc):
                # 如果当前是岛屿，则将当前元素置位海洋，同时将上下左右都置位海洋
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands


so = Solution()
print(so.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]))
