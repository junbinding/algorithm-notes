class Solution:
    """
    67. 二进制求和
    https://leetcode-cn.com/problems/add-binary/
    给你两个二进制字符串，返回它们的和（用二进制表示）。
    输入为 非空 字符串且只包含数字 1 和 0。
    """
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b

        if not b:
            return a

        res = ''
        ext = 0
        i = 0
        a_len = len(a)
        b_len = len(b)
        while i < a_len or i < b_len:
            tmp_sum = ext
            if i < b_len and i < a_len:
                tmp_sum += int(a[a_len - 1 - i]) + int(b[b_len - 1 - i])
            elif i < b_len:
                tmp_sum += int(b[b_len - 1 - i])
            else:
                tmp_sum += int(a[a_len - 1 - i])

            ext = 1 if tmp_sum >= 2 else 0
            if tmp_sum >= 2:
                tmp_sum -= 2
            res = str(tmp_sum) + res
            i += 1
        if ext:
            res = str(ext) + res
        return res


so = Solution()
# 100
print(so.addBinary('11', '1'))
# 10101
print(so.addBinary('1010', '1011'))