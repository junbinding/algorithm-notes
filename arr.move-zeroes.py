from typing import List

class Solution:
    """
    283. 移动零
    https://leetcode-cn.com/problems/move-zeroes/
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    Do not return anything, modify nums in-place instead.
    """
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1


so = Solution()
nums = [0, 1, 0, 3, 12]
so.moveZeroes(nums)
print(nums)

