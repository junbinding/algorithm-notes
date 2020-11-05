from typing import List

class Solution:
    """
    84. 柱状图中最大的矩形
    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
    求在该柱状图中，能够勾勒出来的矩形的最大面积。
    """
    # 单调栈，单向递增栈，只要找到每根柱子左右两边第一个小于当前柱子高度的作为左右边界
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            # 如果新元素小于栈顶元素
            while heights[i] < heights[stack[-1]]:
                # 弹出栈顶元素
                cur_height = heights[stack.pop()]
                # i是栈顶元素的右边界，即右边第一个小于栈顶元素的高度
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res

    # 暴力破解，找每根柱子的左右边界
    def largestRectangleAreaByForce(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 0:
            return 0

        if length == 1:
            return heights[0]

        res = 0
        for i in range(length):
            # 找左边最后一个大于等于heights[i]的下标
            left = i
            while left > 0 and heights[left - 1] >= heights[i]:
                left -= 1

            # 找右边最后一个大于等于heights[i]的下标
            right = i
            while right < length - 1 and heights[right + 1] >= heights[i]:
                right += 1

            width = right - left + 1
            res = max(res, width * heights[i])

        return res
    # 暴力破解，穷举
    def largestRectangleAreaByExhaustive(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        maxRes = 0
        for i in range(len(heights)):
            minHeight = heights[i]
            maxRes = max(minHeight, maxRes)
            if (i + 1) == len(heights): break
            for j in range(i + 1, len(heights)):
                minHeight = min(minHeight, heights[j])
                maxRes = max(minHeight * (j - i + 1), maxRes)

        return maxRes


so = Solution()
print(so.largestRectangleArea([1, 2, 7, 8, 9, 2, 3]))
