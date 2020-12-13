
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    160. 相交链表
    https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
    编写一个程序，找到两个单链表相交的起始节点。
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA


