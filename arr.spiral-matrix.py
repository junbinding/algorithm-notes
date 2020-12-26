from typing import List

class Solution:
    """
    54. 螺旋矩阵
    https://leetcode-cn.com/problems/spiral-matrix/
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0:
            return result

        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        x, y = 0, 0
        while left <= right and up <= down:
            # 向右移动
            y = left
            while y <= right and self.avoid(left, right, up, down):
                result.append(matrix[x][y])
                y += 1
            y -= 1
            up += 1

            # 向下移动
            x = up
            while x <= down and self.avoid(left, right, up, down):
                result.append(matrix[x][y])
                x += 1
            x -= 1
            right -= 1

            # 向左移动
            y = right
            while y >= left and self.avoid(left, right, up, down):
                result.append(matrix[x][y])
                y -= 1
            y += 1
            down -= 1

            # 向上移动
            x = down
            while x >= up and self.avoid(left, right, up, down):
                result.append(matrix[x][y])
                x -= 1
            x += 1
            left += 1
        return result

    def avoid(self, left, right, up, down):
        return left <= right and up <= down


so = Solution()
# [1,2,3,6,9,8,7,4,5]
print(so.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

