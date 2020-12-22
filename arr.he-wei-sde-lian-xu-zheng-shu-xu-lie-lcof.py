from typing import List

class Solution:
    """
    剑指 Offer 57 - II. 和为s的连续正数序列
    https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
    输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
    序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
    """
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 定义快指针
        i = 1
        # 定义慢指针
        j = 1
        res = []
        win = 0
        arr = list(range(1, target + 1))
        # 慢指针超过中值，则结果不符合
        while j <= target / 2:
            if win < target:
                win += i
                i += 1
            elif win > target:
                win -= j
                j += 1
            else:
                res.append(arr[j-1:i-1])
                win -= j
                j += 1
        return res


so = Solution()
print(so.findContinuousSequence(9))