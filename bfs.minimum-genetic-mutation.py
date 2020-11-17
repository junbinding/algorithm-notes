from typing import List

class Solution:
    """
    433. 最小基因变化
    https://leetcode-cn.com/problems/minimum-genetic-mutation/
    一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
    假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
    例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
    与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
    现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。
    """
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        possible = ['A', 'C', 'G', 'T']
        # 定义初始队列
        queue = [(start, 0)]
        while queue:
            # 定义终止条件
            word, step = queue.pop(0)
            if word == end:
                return step
            # 在 bank 中寻找相差一位的
            for i in range(len(word)):
                for p in possible:
                    tmp = word[:i] + p + word[i+1:]
                    if tmp in bank:
                        bank.remove(tmp)
                        queue.append((tmp, step + 1))
        return -1


so = Solution()
print(so.minMutation("AAAACCCC", 'CCCCCCCC', ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))
