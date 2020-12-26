from typing import List


class Solution:
    """
    154. 寻找旋转排序数组中的最小值 II
    https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    注意数组中可能存在重复的元素。
    """
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            # 左侧是单调的，旋转发生在右侧
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1

        return nums[l]


    def findMinByForce(self, nums: List[int]) -> int:
        for num in nums:
            if num < nums[0]:
                return num

        return nums[0]


so = Solution()
# print(so.findMin([3,4,5,1,2]))
print(so.findMin([3,3,1,3]))
