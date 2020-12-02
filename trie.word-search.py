from typing import List


class Solution:
    """
    79. 单词搜索
    https://leetcode-cn.com/problems/word-search/
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        # 定义方向，上下右左
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 检查是否存在，i,j 是 board 的位置，k 是 word 的位置
        def check(i: int, j: int, k: int) -> bool:
            # 如果发现不匹配，则返回 False
            if board[i][j] != word[k]:
                return False
            # 如果到了最后一位，则返回 True
            if k == len(word) - 1:
                return True

            # 添加已访问过
            visited.add((i, j))
            result = False
            # 遍历方向
            for di, dj in directions:
                # 遍历周围位置
                newi, newj = i + di, j + dj
                # 判断位置是否越界
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    # 如果没有被访问过
                    if (newi, newj) not in visited:
                        # 继续稽查周围的
                        if check(newi, newj, k + 1):
                            result = True
                            break
            # 回复状态
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        # 检查每个点开始
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


so = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(so.exist(board, 'ABCCEDF'))
