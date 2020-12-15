class Solution:
    """
    6. Z 字形变换
    https://leetcode-cn.com/problems/zigzag-conversion/
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排
    """
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if numRows <= 1:
            return s

        res = ['' for _ in range(numRows)]
        p = 2 * numRows - 2
        for i in range(l):
            remainder = i % p
            if remainder < numRows:
                res[remainder] += s[i]
            else:
                res[p - remainder] += s[i]
        return ''.join(res)


so = Solution()
# LCIRETOESIIGEDHN
print(so.convert('LEETCODEISHIRING', 3))
# LDREOEIIECIHNTSG
print(so.convert('LEETCODEISHIRING', 4))
print(so.convert('A', 1))
