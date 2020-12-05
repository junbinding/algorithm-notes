class Solution:
    """
    191. 位1的个数
    https://leetcode-cn.com/problems/number-of-1-bits/
    编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
    """
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1

        return count


so = Solution()
print(so.hammingWeight(0o11111111111111111111111111111101))
