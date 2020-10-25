
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    25. K 个一组翻转链表
    https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
    """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, end = dummy, dummy
        while end is not None:
            i = 0
            # 循环获取待处理的最后一个节点
            while i < k and end:
                end = end.next
                i += 1

            # 如果没有，则代表最后一轮不足 k 个，不用处理
            if not end: break

            # 断开链表
            start = pre.next
            next = end.next
            end.next = None

            # 翻转数组
            pre.next = self.reverse(start)
            start.next = next

            # 进行下一组处理
            pre = start
            end = pre
        return dummy.next

    def reverse(self, head):
        pre = None
        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

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
# node = so.reverseList()
params = [1, 2, 3, 4, 5, 6, 7, 8]

# 打印链表
def printList(link):
    print(link.val)
    while(link.next is not None):
        link = link.next
        print(link.val)

printList(so.reverse(so.convertArr2Link(params)))

