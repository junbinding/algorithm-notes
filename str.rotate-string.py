class Solution:
    """
    796. 旋转字符串
    https://leetcode-cn.com/problems/rotate-string/
    给定两个字符串, A 和 B。
    A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
    """
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and A in (B * 2)


so = Solution()
print(so.rotateString('abcde', 'abced'))