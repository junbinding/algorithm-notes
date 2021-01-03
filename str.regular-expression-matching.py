from functools import lru_cache

class Solution:
    """
    10. 正则表达式匹配
    https://leetcode-cn.com/problems/regular-expression-matching/
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串
    """
    def isMatch(self, s: str, p: str) -> bool:
        # i 记录 s 的位置，j 记录 p 中的位置
        @lru_cache(None)
        def recur(i, j):
            # 结束条件
            if j == len(p):
                return i == len(s)

            # 首字母匹配
            first_match = (len(s) > i) and (p[j] == s[i] or p[j] == '.')

            # 处理 `*`
            if len(p) >= j + 2 and p[j + 1] == '*':
                return recur(i, j + 2) or (first_match and recur(i + 1, j))

            # 处理首字母匹配
            return first_match and recur(i + 1, j + 1)

        return recur(0, 0)


so = Solution()
# True
print(so.isMatch('aab', 'c*a*b'))
# False
print(so.isMatch('mississippi', 'mis*is*p*.'))