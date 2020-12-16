# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    19. 删除链表的倒数第N个节点
    https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 定义哨兵节点
        res = ListNode()
        res.next = head
        # 定义要删除元素的前一个元素
        pre = ListNode()
        # 定义当前元素
        cur = res
        # head 元素是第一个，所以从1开始
        i = 1
        while head:
            if i >= n:
                pre = cur
                cur = cur.next

            head = head.next
            i += 1

        pre.next = cur.next
        return res.next



