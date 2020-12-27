class Solution:
    """
    12. 整数转罗马数字
    https://leetcode-cn.com/problems/integer-to-roman/
    罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
    给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
    """
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = ''
        while index < 13:
            if num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            else:
                index += 1

        return res


so = Solution()
print(so.intToRoman(58))