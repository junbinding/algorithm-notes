
class Solution:
    """
    242. 有效的字母异位词
    https://leetcode-cn.com/problems/valid-anagram/description/
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    """
    # map 方法
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                m[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in m:
                return False
            else:
                m[t[j]] -= 1

        for v in m.values():
            if v != 0:
                return False
        return True


    # 排序
    def isAnagramBySort(self, s: str, t: str) -> bool:
        s_sorted = ''.join(sorted(s))
        t_sorted = ''.join(sorted(t))
        return s_sorted == t_sorted



so = Solution()
print(so.isAnagram('aa', 'bb'))