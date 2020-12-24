from typing import List


class Solution:
    """
    136. 只出现一次的数字
    https://leetcode-cn.com/problems/single-number/
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
    找出那个只出现了一次的元素。
    """
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res


so = Solution()
print(so.singleNumber([4,1,2,1,2]))
