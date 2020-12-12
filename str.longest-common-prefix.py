from typing import List

class Solution:
    """
    14. 最长公共前缀
    https://leetcode-cn.com/problems/longest-common-prefix/
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        if len(strs) == 1:
            return strs[0]

        res = ''
        first = strs[0]
        for s in range(len(strs[0])):
            for p in range(1, len(strs)):
                if s < len(strs[p]) and first[s] == strs[p][s]:
                    continue
                else:
                    return res
            res += first[s]
        return res


so = Solution()
print(so.longestCommonPrefix(["flower","flow","flight"]))
