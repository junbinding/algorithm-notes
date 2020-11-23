from typing import List


class Solution:
    """
    455. 分发饼干
    https://leetcode-cn.com/problems/assign-cookies/description/
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
    对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
    如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()

        idx = len(s) - 1
        for i in range(len(g) - 1, -1, -1):
            if idx >= 0 and s[idx] >= g[i]:
                res += 1
                idx -= 1

        return res

    def findContentChildrenByForce(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        m = 0
        for i in range(len(s)):
            for j in range(m, len(g)):
                if s[i] >= g[j]:
                    res += 1
                    m = j + 1
                    break

        return res


so = Solution()
print(so.findContentChildren([10,9,8,7],[5,6,7,8]))

