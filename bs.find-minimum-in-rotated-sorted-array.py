from typing import List


class Solution:
    """
    153. 寻找旋转排序数组中的最小值
    https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
    请找出其中最小的元素。
    """
    def findMin(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 1:
            return nums[0]

        res = nums[0]
        l, r = 0, m - 1
        while l <= r:
            mid = l + (r - l) // 2
            res = min(nums[mid], res)
            # 如果左侧单调
            if nums[l] <= nums[mid]:
                res = min(nums[l], res)
                l = mid + 1
            # 如果右侧单调
            else:
                res = min(nums[mid + 1], res)
                r = mid - 1

        return res


so = Solution()
# print(so.findMin([3,4,5,1,2]))
# print(so.findMin([4,5,6,7,0,1,2]))
print(so.findMin([3, 1, 2]))
