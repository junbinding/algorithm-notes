from typing import List


class Solution:
    """
    22. 括号生成
    https://leetcode-cn.com/problems/generate-parentheses/
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    """
    # dfs
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ''

        def dfs(left, right, cur):
            if left == 0 and right == 0:
                res.append(cur)
                return

            if right < left:
                return

            if left > 0:
                dfs(left - 1, right, cur + '(')

            if right > 0:
                dfs(left, right - 1, cur + ')')

        dfs(n, n, cur)
        return res


so = Solution()
print(so.generateParenthesis(3))
