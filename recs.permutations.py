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
        l = len(nums)

        def backtrack(first):
            if first == l:
                res.append(nums[:])
                return
            for i in range(first, l):
                # 置换
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                # 恢复
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return res


so = Solution()
print(so.permute([1, 1, 2]))
