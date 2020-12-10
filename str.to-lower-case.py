class Solution:
    """
    709. 转换成小写字母
    https://leetcode-cn.com/problems/to-lower-case/
    实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
    """
    def toLowerCase(self, str: str) -> str:
        if not str or len(str) == 0:
            return str

        res = []
        for i in str:
            if 65 <= ord(i) <= 90:
                res.append(chr(ord(i) + 32))
            else:
                res.append(i)

        return ''.join(res)


so = Solution()
print(so.toLowerCase('Hello'))
