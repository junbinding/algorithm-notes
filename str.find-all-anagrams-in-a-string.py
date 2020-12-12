from typing import List

class Solution:
    """
    438. 找到字符串中所有字母异位词
    https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
    给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
    字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
    说明：
    - 字母异位词指字母相同，但排列不同的字符串。
    - 不考虑答案输出的顺序。
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        # 定义窗口
        window = {}
        # 定义目标传 map
        needs = {}

        # 构件目标传
        for c in p:
            needs[c] = needs.get(c, 0) + 1

        length, limit = len(p), len(s)
        left = right = 0
        # 如果右指针小于边界
        while right < limit:
            c = s[right]
            # 如果出现了字符不在目标串中
            if c not in needs:
                window.clear()
                left = right = right + 1
            else:
                # 加入窗口中最右侧元素
                window[c] = window.get(c, 0) + 1
                # 如果位数匹配
                if right - left + 1 == length:
                    if window == needs:
                        res.append(left)
                    # 移除原先的最左侧元素
                    window[s[left]] -= 1
                    # 窗口向右移
                    left += 1
                right += 1
        return res

    # 暴力简单
    def findAnagramsByForce(self, s: str, p: str) -> List[int]:
        res = []
        p_str = ''.join(sorted(p))
        window, length = len(p), len(s)
        i = 0
        while i <= length - window:
            tmp = s[i:i+window]
            if ''.join(sorted(tmp)) == p_str:
                res.append(i)
            i += 1
        return res


so = Solution()
# [0, 6]
# print(so.findAnagrams('cbaebabacd', 'abc'))
# [0, 1, 2]
print(so.findAnagrams('abab', 'ab'))
