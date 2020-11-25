from typing import List


class Solution:
    """
    74. 搜索二维矩阵
    https://leetcode-cn.com/problems/search-a-2d-matrix
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 定义行数
        m = len(matrix)
        if m == 0:
            return False

        # 定义列数
        n = len(matrix[0])

        # 定义二分查找左右边界
        l, r = 0, m * n - 1
        while l <= r:
            mid_idx = (l + r) // 2
            # // 标识整除，等到中位数的行数，然后取模得到列数
            mid_ele = matrix[mid_idx // n][mid_idx % n]

            if target == mid_ele:
                return True

            if mid_ele < target:
                l = mid_idx + 1
            else:
                r = mid_idx - 1

        return False


so = Solution()
print(so.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 20))

print()
