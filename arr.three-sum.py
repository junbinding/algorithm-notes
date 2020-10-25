from typing import List

class Solution:
    """
    15. 三数之和
    https://leetcode-cn.com/problems/3sum/
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
    """
    # 双指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 若数组长度小于3，则返回空数组
        res = []
        n = len(nums)
        if n < 3:
            return res

        # 对数组进行排序
        nums.sort()
        for i in range(n-2):
            # 若 i 大于 0 则终止循环，返回结果
            if nums[i] > 0:
                return res


            # 对于重复元素，直接跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 声明左指针 L=i+1, 右指针 R=n-1,
            l = i + 1
            r = n - 1

            while(l < r):
                num = nums[i] + nums[l] + nums[r]
                # 若 nums[i] + nums[L] + nums[R] = 0
                if num == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                # 若和小于0，则说明 nums[L] 小了，L 向右移
                elif num < 0:
                    l += 1
                # 若和大于0，则说明 nums[R] 打了，R 向左移
                else:
                    r -= 1
        return res

    # 暴力破解
    def threeSumByForce(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for m in range(j + 1, len(nums)):
                    if m > j + 1 and nums[m] == nums[m - 1]:
                        continue
                    if nums[i] + nums[j] + nums[m] == 0:
                        res.append([nums[i], nums[j], nums[m]])
        return res


so = Solution()
print(so.threeSum([-1,0,1,2,-1,-4]))
print(so.threeSum([0, 0, 0, 0]))
print(so.threeSum([-2,0,0,2,2]))

