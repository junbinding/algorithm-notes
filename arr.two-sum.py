from typing import List


class Solution:
    """
    1. 两数之和
    https://leetcode-cn.com/problems/two-sum/
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
    """
    # hash map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if map.get(target - num) is not None:
                return [map.get(target - num), i]
            map[num] = i

        return []

    # 暴力破解
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target :
                    res = [i, j]
                    break

        return res


so = Solution()
print(so.twoSum(nums=[2, 7, 11, 15], target=9))

