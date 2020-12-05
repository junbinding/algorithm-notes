from typing import List

class Solution:
    """
    338. 比特位计数
    https://leetcode-cn.com/problems/counting-bits/description/
    给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
    """
    def countBits(self, num: int) -> List[int]:
        dp = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1

        return dp



so = Solution()
# [0, 1, 1, 2, 1, 2]
print(so.countBits(5))
