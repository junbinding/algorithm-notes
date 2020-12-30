from typing import List


class Solution:
    """
    剑指 Offer 40. 最小的k个数
    https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
    输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


so = Solution()
print(so.getLeastNumbers([0,1,2,1], 2))