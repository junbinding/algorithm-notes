from typing import List


class Solution:
    """
    189. 旋转数组
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    https://leetcode-cn.com/problems/rotate-array/
    """
    # 翻转
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # 拼接
    def rotateByConcat(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # 插入法
    def rotateByInsert(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())


so = Solution()
print(so.rotate([1, 1, 2, 3 , 3, 4, 5], 3))

