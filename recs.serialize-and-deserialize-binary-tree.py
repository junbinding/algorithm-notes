
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
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null,'

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + right


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        return self.build_tree(l)

    def build_tree(self, data):
        if not data:
            return
        val = data.pop(0)
        if val == 'null': return None
        node = TreeNode(val)
        node.left = self.build_tree(data)
        node.right = self.build_tree(data)
        return node

so = Codec()

print(so.serialize(so.deserialize('1,2,3,null,null,4,5')))

