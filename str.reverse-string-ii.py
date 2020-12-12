class Solution:
    """
    541. 反转字符串 II
    https://leetcode-cn.com/problems/reverse-string-ii/
    给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
    如果剩余字符少于 k 个，则将剩余字符全部反转。
    如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
    """
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0, len(arr), 2 * k):
            arr[i:i+k] = reversed(arr[i:i+k])

        return ''.join(arr)

so = Solution()
print(so.reverseStr('abcd', 3))