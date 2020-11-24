from typing import List


class Solution:
    """
    45. 跳跃游戏 II
    https://leetcode-cn.com/problems/jump-game-ii/
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    """
    def jump(self, nums: List[int]) -> int:
        res = 0
        # 定义结束最小路径的暂停点
        end = 0
        # 最远距离
        max_pos = 0

        for i in range(len(nums) - 1):
            # 当前最远跳动范围
            max_pos = max(nums[i] + i, max_pos)
            # 如果当前移动到暂停点，则将移动到下一个暂停点
            if i == end:
                end = max_pos
                res += 1

        return res


so = Solution()
print(so.jump([3,2,1,0,4]))
