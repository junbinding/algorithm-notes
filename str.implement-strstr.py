class Solution:
    """
    28. 实现 strStr()
    https://leetcode-cn.com/problems/implement-strstr
    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0

        if len(haystack) < len(needle):
            return -1

        origin_len = len(haystack)
        aim_len = len(needle)
        origin_idx = 0
        aim_idx = 0

        while aim_idx < aim_len:
            # 判断是否结束
            if origin_idx > origin_len - 1:
                return -1
            # 如果匹配相等，则都前进1位
            if needle[aim_idx] == haystack[origin_idx]:
                origin_idx += 1
                aim_idx += 1
            else:
                # 查找下一个字符的位置
                next_char_at = origin_idx - aim_idx + aim_len
                # 如果下一个字符超出，则返回 -1
                if next_char_at < origin_len:
                    # 在目标串中匹配下一个字符
                    aim_last_idx = needle.rfind(haystack[next_char_at])
                    # 没找到则再往后移一位
                    if aim_last_idx == -1:
                        origin_idx = next_char_at + 1
                    # 找到了，则更新原串的下标
                    else:
                        origin_idx = next_char_at - aim_last_idx
                    # 更新目标串
                    aim_idx = 0
                else:
                    return -1
        return origin_idx - aim_idx

    def strStrByForce(self, haystack: str, needle: str) -> int:
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
# print('abc'[2])
