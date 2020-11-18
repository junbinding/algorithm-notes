from typing import List

class Solution:
    """
    TODO
    126. 单词接龙 II
    https://leetcode-cn.com/problems/word-ladder-ii/description/
    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换后得到的单词必须是字典中的单词。
    """
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        pass


so = Solution()
print(so.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
