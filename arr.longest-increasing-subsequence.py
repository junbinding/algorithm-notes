from typing import List


class Solution:
    """
    300. 最长递增子序列
    https://leetcode-cn.com/problems/longest-increasing-subsequence
    给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
    子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = len(nums)
        # 定义当前元素为最后的状态数组
        dp = [1] * l
        for i in range(0, l):
            for j in range(i):
                # 只有前面的数字小于当前数字，才会形成严格递增
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



so = Solution()
print(so.lengthOfLIS([1,3,6,7,9,4,10,5,6]))