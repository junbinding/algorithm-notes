from typing import List


class Solution:
    """
    547. 朋友圈
    https://leetcode-cn.com/problems/friend-circles/
    班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
    """
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 总共 len(M) 个人
        p = [i for i in range(len(M))]
        # 最多有 len(M) 个关系，即每个人都不好朋友
        res = len(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    res = self.union(p, i, j, res)
        return res

    def union(self, p, i, j, res):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        # 如果这两个人的代表是同一个人，则陌生关系数量不变
        if p1 == p2:
            return res
        # 如果这两个是朋友，则关系熟减一
        p[p1] = p2
        return res - 1

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        return root


so = Solution()
print(so.findCircleNum([
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]))
