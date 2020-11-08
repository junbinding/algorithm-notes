from typing import List


class Solution:
    """
    22. 括号生成
    https://leetcode-cn.com/problems/generate-parentheses/
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    """
    arr = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.arr = []
        self._gen(0, 0, n * 2, '')
        return self.arr


    def _gen(self, left, right, max, s):
        # 终止条件
        if len(s) == max:
            self.arr.append(s)
            return s

        # 递归
        if left < max / 2:
            self._gen(left + 1, right, max, s + '(')
        if left > right:
            self._gen(left, right + 1, max, s + ')')


so = Solution()
print(so.generateParenthesis(1))