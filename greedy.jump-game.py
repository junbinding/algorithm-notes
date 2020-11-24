from typing import List


class Solution:
    """
    55. 跳跃游戏
    https://leetcode-cn.com/problems/jump-game/
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。
    """
    def canJump(self, nums: List[int]) -> bool:
        # 定义能跳到最远的下标
        k = 0
        for i in range(len(nums)):
            # 最远的距离
            if i > k:
                return False

            # 更新能跳最远的下标
            k = max(k, i + nums[i])

        return True


so = Solution()
print(so.canJump([3,2,1,0,4]))
