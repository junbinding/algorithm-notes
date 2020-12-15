from typing import List

class Solution:
    """
    14. 最长公共前缀
    https://leetcode-cn.com/problems/longest-common-prefix/
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        print(str0, str1)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

    def longestCommonPrefixByFind(self, strs: List[str]) -> str:
        if not strs:
            return ''

        pre = strs[0]
        # 遍历数组
        for i in range(1, len(strs)):
            while strs[i].find(pre) != 0:
                if len(pre) == 0:
                    return ''
                pre = pre[:-1]
        return pre

    def longestCommonPrefixByForce(self, strs: List[str]) -> str:
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
print(so.longestCommonPrefix(["flower","flew","fleght"]))
