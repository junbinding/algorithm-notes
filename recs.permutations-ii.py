from typing import List


class Solution:
    """
    47. 全排列 II
    https://leetcode-cn.com/problems/permutations-ii/
    给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
    """
    # 回溯法
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                # 置换
                used[i] = True
                path.append(nums[i])
                backtrack(depth+1, path)
                # 恢复
                used[i] = False
                path.pop()

        backtrack(0, [])
        return res


so = Solution()
print(so.permuteUnique([1,0,0,9]))

