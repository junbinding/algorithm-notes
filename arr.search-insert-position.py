from typing import List

class Solution:
    """
    35. 搜索插入位置
    https://leetcode-cn.com/problems/search-insert-position/
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = len(nums)
        if not s:
            return 0

        if nums[s - 1] < target:
            return s

        l = 0
        r = s - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l


so = Solution()
print(so.searchInsert([1, 3, 5, 6], 2))
