from typing import List


class Solution:
    """
    137. 只出现一次的数字 II
    https://leetcode-cn.com/problems/single-number-ii/
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
    """
    def singleNumber(self, nums: List[int]) -> int:
        tmp_map = {}
        for num in nums:
            tmp_map[num] = tmp_map.get(num, 0) + 1

        for k, v in tmp_map.items():
            if v == 1:
                return k

        return 0



so = Solution()
print(so.singleNumber([0,1,0,1,0,1,99]))