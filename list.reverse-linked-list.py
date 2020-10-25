
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    206. 反转链表
    https://leetcode-cn.com/problems/reverse-linked-list/
    反转一个单链表。
    """
    # 双指针
    def reverseList(self, head: ListNode)-> ListNode:
        pre = None
        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


    # 暴力破解
    def reverseListByForce(self, head: ListNode) -> ListNode:
        if head is None:
            return
        res_arr = []
        while head is not None:
            res_arr.append(head.val)
            head = head.next

        res_arr.reverse()

        return self.convertArr2Link(res_arr)

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
params = [1, 2, 3, 4, 5]

# 打印链表
def printList(link):
    print(link.val)
    while(link.next is not None):
        link = link.next
        print(link.val)

printList(so.reverseList(so.convertArr2Link(params)))

