class Solution:
    """
    3. 无重复字符的最长子串
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    """
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        if n <= 1:
            return n

        left = 0
        # 记录集合
        lookup = set()
        # 最大宽度
        max_len = 0
        # 目前宽度
        cur_len = 0
        for i in range(n):
            cur_len += 1
            # 如果最新元素在集合中，则必须移除掉该元素
            while s[i] in lookup:
                # 移除第一次出现新元素之前的元素
                lookup.remove(s[left])
                left += 1
                cur_len -= 1

            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

so = Solution()
# 3
print(so.lengthOfLongestSubstring('abcabcbb'))
# 1
print(so.lengthOfLongestSubstring('bbbbb'))
# 3
print(so.lengthOfLongestSubstring('pwwkew'))
# 0
print(so.lengthOfLongestSubstring(''))
