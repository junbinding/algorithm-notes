class Solution:
    """
    917. 仅仅反转字母
    https://leetcode-cn.com/problems/reverse-only-letters/
    给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
    """
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        i = 0
        j = len(arr) - 1
        letters = [chr(i) for i in range(ord('A'), ord('z') + 1) if i <= ord('Z') or i >= ord('a')]
        while i < j:
            if arr[i] in letters and arr[j] in letters:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            elif arr[i] not in letters:
                i += 1
            else:
                j -= 1
        return ''.join(arr)


so = Solution()
print(so.reverseOnlyLetters('Test1ng-Leet=code-Q!'))
