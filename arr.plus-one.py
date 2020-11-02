from typing import List

class Solution:
    """
    66. 加一
    https://leetcode-cn.com/problems/plus-one/
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
    最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            digits[i] += 1
            digits[i] = digits[i] % 10
            # 如果不是0，则代表没有进位
            if digits[i] != 0:
                return digits
            i -= 1

        digits.insert(0, 1)
        return digits

    # 暴力破解
    def plusOneByForce(self, digits: List[int]) -> List[int]:
        res = []
        i = len(digits) - 1
        n = 1
        while i >= 0:
            res.insert(0, (digits[i] + n) % 10)
            n = 1 if (digits[i] + n) > 9 else 0
            i -= 1

        if n > 0:
            res.insert(0, n)
        return res


so = Solution()
print(so.plusOne([9, 9, 9]))
print(so.plusOne([1, 2, 3, 4]))
print(so.plusOne([1, 0]))
print(so.plusOne([1, 0, 1]))

