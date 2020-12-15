from typing import List


class Solution:
    """
    121. 买卖股票的最佳时机
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        dp = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            # 找到最小值
            min_price = min(min_price, prices[i])
            # 找到最大化利润
            dp[i] = max(dp[i-1], prices[i] - min_price)

        return dp[-1]


so = Solution()
print(so.maxProfit([7,1,5,3,6,4]))