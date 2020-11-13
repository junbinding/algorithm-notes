from typing import List

class Solution:
    """
    78. 子集
    https://leetcode-cn.com/problems/subsets/
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    """
    # 回溯
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tmp = []
        res = []
        n = len(nums)
        def dfs(cur):
            if cur == n:
                res.append(tmp[:])
                return
            tmp.append(nums[cur])
            dfs(cur + 1)
            tmp.pop()
            dfs(cur + 1)

        dfs(0)
        return res


so = Solution()
print(so.subsets([1,2,3,4]))
