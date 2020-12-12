class Solution:
    """
    680. 验证回文字符串 Ⅱ
    https://leetcode-cn.com/problems/valid-palindrome-ii/
    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
    """
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        res = 0
        while i < j:
            # 如果相等，则双指针内移一位
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if res == 0:
                    i += 1
                    res += 1
                elif res == 1:
                    i -= 1
                    j -= 1
                    res += 1
                else:
                    return False

        return True


so = Solution()
print(so.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
