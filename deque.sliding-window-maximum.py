from typing import List
from collections import deque

class Solution:
    """
    239. 滑动窗口最大值
    https://leetcode-cn.com/problems/sliding-window-maximum/
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。
    """
    # 双端队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 构造一个单向的队列
        d = deque()
        res = []
        for i, num in enumerate(nums):
            # 每次移动，如果当前的最大值的下标已经被移出窗口了，则踢出掉
            if d and d[0] <= i - k:
                d.popleft()
            # 将小于新进元素的数字全部移除
            while d and nums[d[-1]] < num:
                d.pop()
            # 添加新进元素
            d.append(i)
            # 将最大值添加到结果中
            if i >= k - 1:
                res.append(nums[d[0]])
        return res

    # 暴力求解
    def maxSlidingWindowByForce(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums:
            return res

        tmp_max = max(nums[0:k])
        for i in range(len(nums) - (k - 1)):
            tmp_max = max(nums[i:i+k])
            res.append(tmp_max)
        return res




so = Solution()
print(so.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


