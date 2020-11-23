from typing import List


class Solution:
    """
    860. 柠檬水找零
    https://leetcode-cn.com/problems/lemonade-change/description/
    在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
    顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
    每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
    注意，一开始你手头没有任何零钱。
    如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
    """
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten = 0
        five = 0

        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                ten += 1
                five -= 1
            elif ten > 0 and five > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3

            if five < 0:
                return False

        return True


so = Solution()
print(so.lemonadeChange([5, 5, 5, 10, 20]))
print(so.lemonadeChange([5, 5, 10]))
print(so.lemonadeChange([10, 10]))
print(so.lemonadeChange([5,5,10,10,20]))


