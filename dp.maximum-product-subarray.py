from typing import List
import sys


class Solution:
    """
    152. 乘积最大子数组
    https://leetcode-cn.com/problems/maximum-product-subarray/description/
    给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
    """
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]

        res = -sys.maxsize
        # 维护当前最小值
        cur_min = 1
        # 维护当前最大值
        cur_max = 1

        for i in range(0, len(nums)):
            # 由于存在负数，那么会导致最大的变最小的，最小的变最大的。
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            # 计算最大值
            cur_max = max(cur_max * nums[i], nums[i])
            # 计算最小值
            cur_min = min(cur_min * nums[i], nums[i])
            res = max(res, cur_max)

        return res

so = Solution()
print(so.maxProduct([2, 3, -2, 4, -100]))
