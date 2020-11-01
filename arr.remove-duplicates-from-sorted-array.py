from typing import List


class Solution:
    """
    26. 删除排序数组中的重复项
    给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
    """
    # 双指针
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i = 0
        j = 1
        while j < len(nums):
            # 当快指针等于慢指针的时候，快指针向后移动一位
            # 当快指针不等于慢指针的时候，将快指针和慢指针的后一位交换，两者同时向后移动
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1


so = Solution()
print(so.removeDuplicates([1, 1, 2, 3 , 3, 4, 5]))

