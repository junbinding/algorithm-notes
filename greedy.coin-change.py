import sys
from typing import List


class Solution:
    """
    322. 零钱兑换
    https://leetcode-cn.com/problems/coin-change/
    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
    你可以认为每种硬币的数量是无限的。
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        ans = sys.maxsize

        def changeCoin(amount, idx, count):
            nonlocal ans
            nonlocal coins
            ans = int(ans)
            # 如果是0，则代表循环完成
            if amount == 0:
                ans = min(ans, count)
                return

            # 如果循环到最后，则返回
            if idx == len(coins):
                return

            # 先看看能放几个最大的
            k = int(amount / coins[idx])
            while k >= 0 and k + count < ans:
                # 去除最大的钱币之后
                changeCoin(amount - k * coins[idx], idx + 1, count + k)
                k -= 1

        changeCoin(amount, 0, 0)
        return -1 if ans == sys.maxsize else ans


so = Solution()
print(so.coinChange([1, 2, 5], 11))
print(so.coinChange([8, 2, 5], 11))
print(so.coinChange([2], 3))
print(so.coinChange([1], 0))


"""
void coinChange(vector<int>& coins, int amount, int c_index, int count, int& ans)
{
    if (amount == 0)
    {
        ans = min(ans, count);
        return;
    }
    if (c_index == coins.size()) return;

    for (int k = amount / coins[c_index]; k >= 0 && k + count < ans; k--)
    {
        coinChange(coins, amount - k * coins[c_index], c_index + 1, count + k, ans);
    }
}

int coinChange(vector<int>& coins, int amount)
{
    if (amount == 0) return 0;
    sort(coins.rbegin(), coins.rend());
    int ans = INT_MAX;
    coinChange(coins, amount, 0, 0, ans);
    return ans == INT_MAX ? -1 : ans;
}

作者：ikaruga
链接：https://leetcode-cn.com/problems/coin-change/solution/322-by-ikaruga/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""