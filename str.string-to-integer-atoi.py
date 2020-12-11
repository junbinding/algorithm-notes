class Solution:
    """
    8. 字符串转换整数 (atoi)
    https://leetcode-cn.com/problems/string-to-integer-atoi
    请你来实现一个 atoi 函数，使其能将字符串转换成整数。

    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

    如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
    假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
    该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
    注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

    在任何情况下，若函数不能进行有效的转换时，请返回 0 。
    """
    def myAtoi(self, s: str) -> int:
        res = ''
        s = s.lstrip()
        sym = 1
        num = '0123456789'
        for i in range(len(s)):
            if i == 0 and s[i] == '+':
                continue
            elif i == 0 and s[i] == '-':
                sym = -1
            elif s[i] in num:
                res += s[i]
            else:
                break

        if res == '':
            return 0

        res = int(res) * sym
        if 2147483647 >= res >= - 2147483648:
            return res

        if res >= 0:
            return 2147483647
        else:
            return -2147483648

so = Solution()
print(so.myAtoi('words and 987'))
