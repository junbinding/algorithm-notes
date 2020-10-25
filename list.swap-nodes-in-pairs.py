
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    24. 两两交换链表中的节点
    https://leetcode-cn.com/problems/swap-nodes-in-pairs/
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    """
    def swapPairs(self, head: ListNode)-> ListNode:
        res = pre = ListNode(0)
        pre.next = head
        cur = head
        while cur is not None and cur.next is not None:
            pre.next = cur.next
            tmp_next = cur.next.next
            pre.next.next = cur
            cur.next = tmp_next
            cur = cur.next
            pre = pre.next.next

        return res.next

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
params = [1, 2, 3, 4, 5, 6]

# 打印链表
def printList(link):
    print(link.val)
    while(link.next is not None):
        link = link.next
        print(link.val)

printList(so.swapPairs(so.convertArr2Link(params)))

