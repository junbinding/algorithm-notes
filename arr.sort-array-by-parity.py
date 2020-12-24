from typing import List


class Solution:
    """
    905. 按奇偶排序数组
    https://leetcode-cn.com/problems/sort-array-by-parity/
    给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
    你可以返回满足此条件的任何数组作为答案。
    """
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        j = len(A) - 1
        if j <= 0:
            return A

        i = 0
        while i < j:
            if A[i] % 2 == 1:
                A[j], A[i] = A[i], A[j]
                j -= 1
            else:
                i += 1
        return A


so = Solution()
print(so.sortArrayByParity([3, 1, 2, 4]))