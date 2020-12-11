class Solution:
    """
    387. 字符串中的第一个唯一字符
    https://leetcode-cn.com/problems/first-unique-character-in-a-string/
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
    """
    def firstUniqChar(self, s: str) -> int:
        res = {}
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = [i, 1]
            else:
                res[s[i]][1] += 1

        for i in res:
            if res[i][1] == 1:
                return res[i][0]
        return -1


so = Solution()
print(so.firstUniqChar('cc'))
print('cc'.rfind('c'))