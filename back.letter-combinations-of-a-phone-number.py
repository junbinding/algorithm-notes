from typing import List

class Solution:
    """
    17. 电话号码的字母组合
    https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    """
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        l = len(digits)
        if not l:
            return []

        if l == 1:
            return list(m[digits])

        tmp = []
        res = []
        def dfs(depth):
            if depth == l:
                res.append(''.join(tmp[:]))
                return


            for i in m[digits[depth]]:
                tmp.append(i)
                dfs(depth + 1)
                tmp.pop()
        dfs(0)
        return res

so = Solution()
print(so.letterCombinations('2'))
