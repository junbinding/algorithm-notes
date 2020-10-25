
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    141. 环形链表
    https://leetcode-cn.com/problems/linked-list-cycle/
    给定一个链表，判断链表中是否有环。
    如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
    如果链表中存在环，则返回 true 。 否则，返回 false 。
    """
    # 快慢指针
    def hasCycle(self, head: ListNode)-> bool:
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # Hash
    def hasCycleByMap(self, head: ListNode)-> bool:
        hash = {}
        while head is not None:
            if hash.get(head):
                return True

            hash[head] = 1
            head = head.next
        return False

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

