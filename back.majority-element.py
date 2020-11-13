from typing import List


class Solution:
    """
    169. 多数元素
    https://leetcode-cn.com/problems/majority-element/description/
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
    """
    # 排序
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]

        nums.sort()
        return nums[len(nums) >> 1]


    # 摩尔投票
    def majorityElementByMoore(self, nums: List[int]) -> int:
        # 当长度小于等于2，则多数元素必然为首元素
        if len(nums) <= 2:
            return nums[0]

        # 假定第一个原
        res = nums[0]
        vote = 1

        for i in range(1, len(nums)):
            if nums[i] == res:
                vote += 1
                continue

            vote -= 1
            if vote < 0:
                vote = 1
                res = nums[i]
        return res


    # map 暴力破解
    def majorityElementByForce(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]

        m = {}
        l  = len(nums) / 2
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
                if m[i] >= l:
                    return i
        return nums[0]


so = Solution()
print(so.majorityElement([1, 1, 2, 2, 2]))
