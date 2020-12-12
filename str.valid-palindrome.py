class Solution:
    """
    125. 验证回文串
    https://leetcode-cn.com/problems/valid-palindrome/
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    说明：本题中，我们将空字符串定义为有效的回文串。
    """
    def isPalindrome(self, s: str) -> bool:
        # isalnum: 是否是数字和字母构成
        res = ''.join(ch.lower() for ch in s if ch.isalnum())
        return res == res[::-1]


so = Solution()
print(so.isPalindrome('A man, a plan, a canal: Panama'))
