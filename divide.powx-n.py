class Solution:
    """
    50. Pow(x, n)
    https://leetcode-cn.com/problems/powx-n/
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
    """
    def myPow(self, x: float, n: int) -> float:
        return self.mul(x, n) if n >=0 else 1.0 / self.mul(x, -n)

    def mul(self, x, n):
        if n == 0:
            return 1
        y = self.mul(x, n // 2)
        return y * y if n % 2 == 0 else y * y * x

so = Solution()
print(so.myPow(2, 3))
print(1//2)
