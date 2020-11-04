class Solution:
    """
    20. 有效的括号
    https://leetcode-cn.com/problems/valid-parentheses/
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
    """
    # 栈: 将不同括号分为左右两边，只要是左边则进栈，遇到右边则看是否与栈顶元素匹配。O(n)时间复杂度
    def isValid(self, s: str) -> bool:
        # 如果长度为奇数，则不满足
        if len(s) % 2 != 0:
            return False

        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = list()
        for c in s:
            if c in pairs:
                stack.append(c)
            elif len(stack) > 0 and pairs[stack[-1]] == c:
                stack.pop(-1)
            else:
                return False

        return not stack

    # 暴力破解：通过不断循环清除最小单元，直到没有最小单元，如果剩余字符串长度为0，则满足条件
    def isValidByForce(self, s: str) -> bool:
        while len(s) > 0:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if s.find('{}') == -1 and s.find('[]') == -1 and s.find('()') == -1:
                break

        return len(s) == 0


so = Solution()
print(so.isValid('()[]{}'))
print(so.isValid('([)]{}'))
