from typing import List


class Solution:
    """
    213. 打家劫舍 II
    https://leetcode-cn.com/problems/house-robber-ii
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
    同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
    给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
    """
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            # dp[n] 只与 dp[n-1] 和 dp[n-2] 有关系，因此可以设两个变量 cur和 pre 交替记录
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        # 最终可以分为：没偷最后一间和没偷第一间两种情况
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]


so = Solution()
print(so.rob([1,2,3,1]))

