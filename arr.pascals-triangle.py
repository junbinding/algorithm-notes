from typing import List


class Solution:
    """
    118. 杨辉三角
    https://leetcode-cn.com/problems/pascals-triangle/
    给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
    """
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        i = 0
        while i < numRows:
            if i == 0:
                res.append([1])
                i += 1
                continue

            tmp = []
            j = 0
            while j <= i:
                if j >= len(res[i - 1]) or j == 0:
                    tmp.append(1)
                else:
                    tmp.append(res[i - 1][j] + res[i - 1][j - 1])

                j += 1

            res.append(tmp)
            i += 1

        return res


so = Solution()
print(so.generate(5))