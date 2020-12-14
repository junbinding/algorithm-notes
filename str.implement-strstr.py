class Solution:
    """
    28. 实现 strStr()
    https://leetcode-cn.com/problems/implement-strstr
    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len == needle_len:
            return 0 if needle == haystack else -1

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i

        return -1


so = Solution()
print(so.strStr('abc', 'c'))