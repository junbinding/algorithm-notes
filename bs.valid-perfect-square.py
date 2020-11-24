class Solution:
    """
    367. 有效的完全平方数
    https://leetcode-cn.com/problems/valid-perfect-square/
    给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
    """
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False

        if num <= 1:
            return True

        l, r = 0, num
        while l < r:
            mid = (r + l) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid

        return False

so = Solution()
print(so.isPerfectSquare(16))
print(so.isPerfectSquare(14))
