# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    83. 删除排序链表中的重复元素
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        r = ListNode(None)
        r.next = head
        res = r
        while r and r.next:
            if r.val == r.next.val:
                r.next = r.next.next
                continue

            r = r.next

        return res.next