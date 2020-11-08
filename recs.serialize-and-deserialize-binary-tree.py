from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    297. 二叉树的序列化与反序列化
    https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
    序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
    请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
    """
    # 广度优先
    def serialize(self, root):
        queue = [root]
        res = []

        while queue:
            node = queue.pop(0)
            if node:
                print(node.val)
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                print('null')
                res.append('null')

        return ','.join(res)

    def deserialize(self, data):
        if data == 'null':
            return None

        l = data.split(",")
        root = TreeNode(l[0])
        queue = [root]
        cursor = 1

        while cursor < len(l):
            node = queue.pop(0)
            left_val = l[cursor]
            right_val = l[cursor + 1]

            if left_val != 'null':
                left_node = TreeNode(left_val)
                node.left = left_node
                queue.append(left_node)

            if right_val != 'null':
                right_node = TreeNode(right_val)
                node.right = right_node
                queue.append(right_node)

            cursor += 2

        return root


so = Codec()
print(so.serialize(so.deserialize('1,2,3,null,null,4,5,null,null,null,null')))

print([1, 2, 3,].pop(0))