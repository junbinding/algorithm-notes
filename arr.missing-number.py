from typing import List


class Solution:
    """
    268. 丢失的数字
    https://leetcode-cn.com/problems/missing-number/
    给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
    """
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        # 先求 1..n 之和，然后减去数组中所有的值，剩下的差值就是
        res = (l + 1) * l >> 1

        for num in nums:
            res -= num

        return res


so = Solution()
print(so.missingNumber([9,6,4,2,3,5,7,0,1]))