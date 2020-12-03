from typing import List


class Solution:
    """
    36. 有效的数独
    https://leetcode-cn.com/problems/valid-sudoku
    判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
    1. 数字 1-9 在每一行只能出现一次。
    2. 数字 1-9 在每一列只能出现一次。
    3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 判断行是否满足
        # 判断列是否满足
        col_sets = [set() for _ in range(9)]
        row_sets = [set() for _ in range(9)]
        block_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if board[i][j] in row_sets[i]:
                    return False

                if board[i][j] in col_sets[j]:
                    return False

                if board[i][j] in block_sets[(i // 3) * 3 + j // 3]:
                    return False

                row_sets[i].add(board[i][j])
                col_sets[j].add(board[i][j])
                block_sets[(i // 3) * 3 + j // 3].add(board[i][j])

        return True


so = Solution()
# True
print(so.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

# False
print(so.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
