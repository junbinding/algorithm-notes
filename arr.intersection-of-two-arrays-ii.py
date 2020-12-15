from typing import List


class Solution:
    """
    350. 两个数组的交集 II
    https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
    给定两个数组，编写一个函数来计算它们的交集。
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 循环遍历
        res = []
        for a in nums1:
            if not nums2:
                break

            for j in range(len(nums2)):
                # 如果匹配，则保存结果和移除下标，中断循环
                if nums2[j] == a:
                    res.append(a)
                    nums2.remove(a)
                    break

        return res


so = Solution()
print(so.intersect([4, 5, 9], [9, 4, 9, 8, 4]))