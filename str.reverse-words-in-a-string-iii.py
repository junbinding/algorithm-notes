class Solution:
    """
    557. 反转字符串中的单词 III
    给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
    https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
    """
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return ' '.join(arr)

so = Solution()
print(so.reverseWords('Let\'s take LeetCode contest'))
