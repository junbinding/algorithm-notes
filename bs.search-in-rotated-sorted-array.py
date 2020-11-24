from typing import List

class Solution:
    """
    33. 搜索旋转排序数组
    https://leetcode-cn.com/problems/search-in-rotated-sorted-array
    给你一个整数数组 nums ，和一个整数 target 。
    该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。
    请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

so = Solution()
print(so.search([4,5,6,7,0,1,2], 0))
