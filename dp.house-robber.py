from typing import List


class Solution:
    """
    198. 打家劫舍
    https://leetcode-cn.com/problems/house-robber
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = len(nums)

        if l == 1:
            return nums[0]

        dp = [0] * l
        dp[0] = nums[0]
        dp[1] = nums[1] if nums[1] > nums[0] else nums[0]
        if l <= 2:
            return dp[l - 1]

        for i in range(2, l):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

so = Solution()
# 12
print(so.rob([2, 7, 9, 3, 1]))
