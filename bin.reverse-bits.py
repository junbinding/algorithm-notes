class Solution:
    """
    190. 颠倒二进制位
    https://leetcode-cn.com/problems/reverse-bits/
    颠倒给定的 32 位无符号整数的二进制位。
    """
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1

        return res


so = Solution()
print(so.reverseBits(0o11111111111111111111111111111101))
