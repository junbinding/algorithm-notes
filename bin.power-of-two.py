class Solution:
    """
    231. 2的幂
    https://leetcode-cn.com/problems/power-of-two/
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
    """
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and n & (n - 1) == 0


so = Solution()
print(so.isPowerOfTwo(15))
