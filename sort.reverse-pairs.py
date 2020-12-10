from typing import List


class Solution:
    """
    493. 翻转对
    https://leetcode-cn.com/problems/reverse-pairs/
    给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
    你需要返回给定数组中的重要翻转对的数量。
    """
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = 0

        def merge_sort(arr, left, right):
            nonlocal res
            if left == right:
                return

            mid = left + (right - left) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)

            # i = left
            # j = mid + 1
            # while i <= mid and j <= right:
            #     if arr[i] > 2 * arr[j]:
            #         res += mid - i + 1
            #         j += 1
            #     else:
            #         i += 1

            tmp = [0 for _ in range(right - left + 1)]
            i = left
            j = mid + 1
            idx = 0
            while i <= mid and j <= right:
                if arr[i] < arr[j]:
                    tmp[idx] = arr[i]
                    idx += 1
                    i += 1
                else:
                    tmp[idx] = arr[j]
                    idx += 1
                    j += 1

            while i <= mid:
                tmp[idx] = arr[i]
                idx += 1
                i += 1

            while j <= right:
                tmp[idx] = arr[j]
                idx += 1
                j += 1

            for k in range(left, right + 1):
                arr[k] = tmp[k - left]


        merge_sort(nums, 0, len(nums) - 1)
        return res


so = Solution()
print(so.reversePairs([2,4,3,5,1]))
