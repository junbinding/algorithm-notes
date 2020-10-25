
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    142. 环形链表 II
    https://leetcode-cn.com/problems/linked-list-cycle-ii/
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
    """
    # 快慢指针
    def detectCycle(self, head: ListNode)-> bool:
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


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
params = [1, 2, 3, 4, 5, 2]

print(so.hasCycle(so.convertArr2Link(params)))

