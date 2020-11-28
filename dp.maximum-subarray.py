from typing import List


class Solution:
    """
    53. 最大子序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            # 表示 nums[i] 结尾的最大子序和
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            # 结果未必是以 nums[i] 结尾，所以要取最大值
            res = max(res, dp[i])

        return res



so = Solution()
# 6
print(so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))