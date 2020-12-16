
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    21. 合并两个有序链表
    https://leetcode-cn.com/problems/merge-two-sorted-lists/
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        if not l2:
            return l1

        res = ListNode()
        pre = res
        while l1 and l2:
            if l1.val > l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next

            pre = pre.next

        if l1:
            pre.next = l1

        if l2:
            pre.next = l2

        return res.next

    # 递归
    def mergeTwoListsByRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 暴力破击
    def mergeTwoListsByForce(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = l = ListNode(0)
        while l1 or l2:
            if l1 is not None and l2 is not None:
                if l1.val >= l2.val:
                    l.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    l.next = ListNode(l1.val)
                    l1 = l1.next
            elif l1 is not None:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        return c.next

    # 转换数组到链表
    def convertArr2Link(self, arr):
        if len(arr) == 0:
            return
        res = n = ListNode(0)
        for i in arr:
            n.next = ListNode(i)
            n = n.next

        return res.next


so = Solution()
params1 = [1, 2, 3]
params2 = [1, 2, 3]


print(so.mergeTwoLists(so.convertArr2Link(params1), so.convertArr2Link(params2)))

