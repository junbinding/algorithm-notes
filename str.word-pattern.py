class Solution:
    """
    290. 单词规律
    https://leetcode-cn.com/problems/word-pattern
    给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
    这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        s_arr = s.split(' ')
        if len(s_arr) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in pattern_map and s_arr[i] not in pattern_map.values():
                pattern_map[pattern[i]] = s_arr[i]
            elif pattern_map.get(pattern[i], '') != s_arr[i]:
                return False

        return True

so = Solution()
print(so.wordPattern('abba', 'dog cat cat dog'))
print(so.wordPattern('abba', 'dog cat cat fish'))
print(so.wordPattern('abba', 'dog dog dog dog'))