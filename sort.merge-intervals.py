from typing import List


class Solution:
    """
    56. 合并区间
    https://leetcode-cn.com/problems/merge-intervals/
    给出一个区间的集合，请合并所有重叠的区间。
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. 按照起点排序
        res = []
        cur = -1
        intervals.sort(key=lambda k: k[0])
        # 2. 遍历循环
        for i in range(len(intervals)):
            # 3. 如果第二个值大于前一项的第一个值，则合并区间
            if i == 0 or res[cur][1] < intervals[i][0]:
                res.append(intervals[i])
                cur += 1
            else:
                res[cur][1] = max(res[cur][1], intervals[i][1])

        return res


so = Solution()
print(so.merge([[2,6],[8,10],[15,18],[1,3]]))
