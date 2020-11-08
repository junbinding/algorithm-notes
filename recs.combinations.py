from typing import List


class Solution:
    """
    77. 组合
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
    https://leetcode-cn.com/problems/combinations/
    """
    # 递归
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        if n == 0 or k == 0:
            return res

        nums = range(1, n + 1)

        def backtrace(rest, curr_res, index):
            if len(curr_res) == k:
                res.append(curr_res[:])
                return

            for i in range(index, n):
                # 模拟栈，先选一个数
                curr_res.append(nums[i])
                backtrace(rest[index:], curr_res, i + 1)
                # 执行完成后，推出这个数
                curr_res.pop()

        backtrace(nums, [], 0)
        return res



so = Solution()
print(so.combine(3, 2))
