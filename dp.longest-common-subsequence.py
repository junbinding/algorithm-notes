class Solution:
    """
    1143. 最长公共子序列
    https://leetcode-cn.com/problems/longest-common-subsequence/
    给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
    一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
    若这两个字符串没有公共子序列，则返回 0。
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 构件状态数组
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

    # 暴力求解
    def longestCommonSubsequenceByForce(self, text1: str, text2: str) -> int:
        def dp(i, j):
            # 空串
            if i == -1 or j == -1:
                return 0

            # 找到 lcs 元素
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            # 看看谁的 lcs 最长，就选谁
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        # 首次执行
        return dp(len(text1) - 1, len(text2) - 1)


so = Solution()
print(so.longestCommonSubsequence('abcde', 'ace'))
