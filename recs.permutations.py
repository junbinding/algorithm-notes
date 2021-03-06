from typing import List


class Solution:
    """
    46. 全排列
    https://leetcode-cn.com/problems/permutations/
    给定一个 没有重复 数字的序列，返回其所有可能的全排列。
    """
    # 回溯法
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res

        l = len(nums)
        used = [False] * l
        def backtrack(depth, path):
            if depth == l:
                res.append(path[:])
                return

            for i in range(l):
                if used[i]:
                    continue
                # 置换
                used[i] = True
                path.append(nums[i])
                backtrack(depth + 1, path)
                used[i] = False
                # 恢复
                path.pop()

        backtrack(0, [])
        return res



so = Solution()
print(so.permute([1, 2, 3]))
