from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/remove-element
    27. 移除元素
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        # 定义快指针：标识循环元素的位置
        a = 0
        # 定义慢指针：标识非 val 值的元素位置
        b = 0

        while a < len(nums):
            # 如果非 val，则进行赋值
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b


so = Solution()
print(so.removeElement([0,1,2,2,3,0,4,2], 2))