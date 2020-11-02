from typing import List

class Solution:
    """
    88. 合并两个有序数组
    https://leetcode-cn.com/problems/merge-sorted-array/
    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组
    """
    # 双指针
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[n + m + 1] = nums1[m]
                m -= 1
            else:
                nums1[n + m + 1] = nums2[n]
                n -= 1

    # 系统排序
    def mergeBySystem(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)




so = Solution()
nums = [0, 1, 1, 2, 3, 5, 7]
nums1 = [1, 2, 4]
so.merge(nums, 4, nums1, 3)
print(nums)

