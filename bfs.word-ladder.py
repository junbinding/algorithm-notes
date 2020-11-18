from typing import List
from collections import deque

class Solution:
    """
    127. 单词接龙
    https://leetcode-cn.com/problems/word-ladder/description/
    给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
    a - 每次转换只能改变一个字母。
    b - 转换过程中的中间单词必须是字典中的单词。
    https://leetcode-cn.com/problems/word-ladder/solution/python3-bfshe-shuang-xiang-bfsshi-xian-dan-ci-jie-/
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)

        queue = deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            cur, step = queue.popleft()
            if cur == endWord:
                return step

            for i in range(m):
                for j in range(26):
                    tmp = cur[:i] + chr(97 + j) + cur[i + 1:]
                    if tmp not in visited and tmp in st:
                        queue.append((tmp, step + 1))
                        visited.add(tmp)

        return 0


so = Solution()
# print(so.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
# print(so.ladderLength('hot', 'dog', ["hot","dog"]))
print(so.ladderLength('hot', 'dot', ["hot", "dot","dog"]))
# print(so.ladderLength('a', 'c', ["a", "b","c"]))
# print(so.ladderLength('hot', 'dog', ["hot", "dog","dot"]))


