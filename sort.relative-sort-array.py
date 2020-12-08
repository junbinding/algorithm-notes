from typing import List


class Solution:
    """
    1122. 数组的相对排序
    https://leetcode-cn.com/problems/relative-sort-array/
    给你两个数组，arr1 和 arr2，
    - arr2 中的元素各不相同
    - arr2 中的每个元素都出现在 arr1 中
    对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cur = 0
        ext = len(arr2)
        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    arr1[cur], arr1[j] = arr1[j], arr1[cur]
                    cur += 1
        self.sortRange(arr1, cur, len(arr1) - 1)
        return arr1

    def sortRange(self, arr, left, right):
        if left < right:
            p = self.position(arr, left, right)
            self.sortRange(arr, left, p - 1)
            self.sortRange(arr, p + 1, right)
        return arr

    def position(self, arr, left ,right):
        pivot = left
        idx = pivot + 1
        for i in range(idx, right + 1):
            if arr[i] < arr[pivot]:
                arr[i], arr[idx] = arr[idx], arr[i]
                idx += 1

        arr[pivot], arr[idx - 1] = arr[idx - 1], arr[pivot]
        return idx - 1


so = Solution()
# [2,2,2,1,4,3,3,9,6,7,19]
print(so.relativeSortArray([2,3,1,3,2,4,6,19,9,2,7, 12, 10, 7], [2,1,4,3,9,6]))
