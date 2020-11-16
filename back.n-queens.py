from typing import List

class Solution:
    """
    51. N 皇后
    https://leetcode-cn.com/problems/n-queens/
    n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        pie = set()
        na = set()
        shu = set()
        res = []
        tmp = []
        def dfs(row):
            if row == n:
                res.append(tmp[:])
                return

            for c in range(n):
                if c in shu or c + row in pie or row - c in na:
                    continue

                shu.add(c)
                pie.add(row + c)
                na.add(row - c)
                l = ['.' for i in range(n)]
                l[c] = 'Q'
                tmp.append(''.join(l))
                dfs(row + 1)
                tmp.pop()
                shu.remove(c)
                pie.remove(row + c)
                na.remove(row - c)


        dfs(0)
        return res


so = Solution()
print(so.solveNQueens(3))
