from typing import List


class Solution:
    """
    49. 字母异位词分组
    https://leetcode-cn.com/problems/group-anagrams/
    给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            tmp_str = ''.join(sorted(str))
            if tmp_str not in res:
                res[tmp_str] = [str]
            else:
                res[tmp_str].append(str)

        return list(res.values())


    def groupAnagramsByHash(self, strs: List[str]) -> List[List[str]]:
        res = []
        m = {}
        for str in strs:
            tmp_str = ''.join(sorted(str))
            if tmp_str not in m.keys():
                m[tmp_str] = len(res)
                res.append([])
                res[len(res) - 1].append(str)

            else:
                res[m[tmp_str]].append(str)

        return res



so = Solution()
print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))