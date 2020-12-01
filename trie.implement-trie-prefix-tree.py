class Trie:
    """
    208. 实现 Trie (前缀树)
    https://leetcode-cn.com/problems/implement-trie-prefix-tree/
    实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}

            tree = tree[a]
        tree['#'] = '#'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False

            tree = tree[a]

        if '#' in tree:
            return True

        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False

            tree = tree[a]

        return True


trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
