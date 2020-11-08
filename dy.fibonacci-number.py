class Solution:
    """
    509. 斐波那契数
    https://leetcode-cn.com/problems/fibonacci-number/
    斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
    """
    cache = {}
    def fib(self, N: int) -> int:
        if N < 2:
            return N

        f = 0
        s = 1
        for i in range(2, N+1):
            s = s + f
            f = s - f
        return s

    # 递归
    def fibByRecursive(self, N: int) -> int:
        if N < 2:
            return N

        if N in self.cache:
            return self.cache[N]

        res = self.fib(N - 1) + self.fib(N - 2)
        self.cache[N] = res
        return res

so = Solution()
print(so.fib(10))
