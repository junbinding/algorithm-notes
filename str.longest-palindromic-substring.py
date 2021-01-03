class Solution:
    """
    5. 最长回文子串
    https://leetcode-cn.com/problems/longest-palindromic-substring/
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    """
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l < 2:
            return s

        # 定义状态方程，dp[i][j] 表示 i 到 j 是否是回文串
        dp = [[False] * l for _ in range(l)]

        max_len = 1
        start = 0

        # i 到 i 必然是 True
        for i in range(l):
            dp[i][i] = True

        for j in range(1, l):
            for i in range(0, j):
                # 状态转移方程
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                # 记录开始位置，以及最大长度
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    start = i

        return s[start: start + max_len]


so = Solution()
print(so.longestPalindrome('cbbd'))