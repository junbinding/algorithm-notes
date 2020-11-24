class Solution:
    """
    69. x 的平方根
    https://leetcode-cn.com/problems/sqrtx/
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
    """
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    # 暴力破解
    def mySqrtByForce(self, x: int) -> int:
        if x <= 1:
            return x

        for i in range(1, x//2 + 1):
            if i * i <= x < (i + 1) * (i + 1):
                return i



so = Solution()
print(so.mySqrt(8))
print(so.mySqrt(4))
print(so.mySqrt(2))
print(so.mySqrt(1))
print(so.mySqrt(0))

print(4//2)