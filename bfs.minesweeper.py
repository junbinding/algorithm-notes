from typing import List

class Solution:
    """
    529. 扫雷游戏
    https://leetcode-cn.com/problems/minesweeper/
    给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
    现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：
    1. 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
    2. 如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
    3. 如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
    4. 如果在此次点击中，若无更多方块可被揭露，则返回面板。
    """
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 定义8个方向
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
        # 如果点击区域是雷区，直接返回
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        self.m, self.n = len(board), len(board[0])

        # 计算每个点周边的雷数
        def check(i, j):
            cnt = 0
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == 'M':
                    cnt += 1
            return cnt

        def dfs(i, j):
            cnt = check(i, j)
            if not cnt:
                board[i][j] = 'B'
                for x, y in direction:
                    x, y = x + i, y + j
                    if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == 'E': dfs(x, y)
            else:
                board[i][j] = str(cnt)

        dfs(click[0], click[1])
        return board

so = Solution()
print(so.updateBoard([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']], [3,0]
))
