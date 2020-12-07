class Solution:
    """
    38. 外观数列
    https://leetcode-cn.com/problems/count-and-say/
    给定一个正整数 n ，输出外观数列的第 n 项。
    「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
    你可以将其视作是由递归公式定义的数字字符串序列：
    countAndSay(1) = "1"
    countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
    """
    def countAndSay(self, n: int) -> str:
        dp = ['' for _ in range(n)]
        i = 0
        while i < n:
            if i == 0:
                dp[i] = '1'
                i += 1
                continue
            res = ''
            tmp = (dp[i-1][0], 0)
            for j in range(len(dp[i - 1])):
                if dp[i - 1][j] == tmp[0]:
                    tmp = (tmp[0], tmp[1] + 1)
                else:
                    res = res + str(tmp[1]) + tmp[0]
                    tmp = (dp[i - 1][j], 1)

                if j == len(dp[i - 1]) - 1:
                    res = res + str(tmp[1]) + tmp[0]

            dp[i] = res
            i += 1
        return dp[-1]


so = Solution()
# 1211
print(so.countAndSay(4))
# 111221
print(so.countAndSay(5))
# 312211
print(so.countAndSay(25))
