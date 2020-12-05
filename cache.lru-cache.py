class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:
    """
    146. LRU 缓存机制
    https://leetcode-cn.com/problems/lru-cache
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
    实现 LRUCache 类：
    1. LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
    2. int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    3. void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
    """
    def __init__(self, capacity: int):
        self.dict = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def insert(self, node):
        # 前置
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.delete(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.delete(node)
            self.insert(node)
            return

        if len(self.dict) == self.capacity:
            node = self.tail.prev
            self.delete(node)
            del self.dict[node.key]

        node = Node(key, value)
        self.dict[key] = node
        self.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)