class Solution:
    """
    650. 只有两个键的键盘
    https://leetcode-cn.com/problems/2-keys-keyboard/
    最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
        Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
        Paste (粘贴) : 你可以粘贴你上一次复制的字符。
    给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
    """
    def minSteps(self, n: int) -> int:
        # 如果是质数，则是他本身
        # 如果是合数，则是分解到所有不能再分解的质数的操作次数的和
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n = n // i

        return res


so = Solution()
# 3
print(so.minSteps(21))
