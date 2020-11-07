from typing import List

class Solution:
    """
    42. 接雨水
    https://leetcode-cn.com/problems/trapping-rain-water/
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    """
    # 双指针
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        if n == 0:
            return res

        l_max = height[0]
        r_max = height[n - 1]
        # 定义左指针
        l = 0
        # 定义右指针
        r = n - 1

        while l <= r:
            # 获取左边最大值
            l_max = max(l_max, height[l])
            # 获取右边最大值
            r_max = max(r_max, height[r])

            # 当左边最大值小于右边最大值，则最多盛水 l_max - height[i]
            if l_max < r_max:
                res += l_max - height[l]
                l += 1
            else:
                res += r_max - height[r]
                r -= 1

        return res

    # 备忘录方式：计算并缓存住每个位置左右两侧的最大高度
    def trapByNote(self, height: List[int]) -> int:
        res = 0
        if not height:
            return res
        length = len(height)
        l_max = [0] * length
        r_max = [0] * length
        l_max[0] = height[0]
        r_max[length - 1] = height[length - 1]

        # 从左向右计算 l_max
        for i in range(1, length):
            l_max[i] = max(height[i], l_max[i-1])

        # 从右向左计算 r_max
        for i in range(length-2, 0, -1):
            r_max[i] = max(height[i], r_max[i+1])

        # 计算每个高度
        for i in range(1, length - 1):
            res += min(l_max[i], r_max[i]) - height[i]

        return res

    # 暴力破解：获取每根柱子可以盛放的水
    def trapByForce(self, height: List[int]) -> int:
        length = len(height)
        res = 0
        for i in range(1, length - 1):
            l_max = 0
            r_max = 0
            # 获取右侧的最大高度
            for j in range(i, length):
                r_max = max(r_max, height[j])

            # 获取左侧的最大高度
            for k in range(0, i):
                l_max = max(l_max, height[k])

            # 相对较小的高度减去当前柱子的高度，就是当前柱子可盛放的高度
            tmp_res = min(l_max, r_max) - height[i]
            res += tmp_res if tmp_res >= 0 else 0

        return res


so = Solution()
# result is 9
print(so.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
