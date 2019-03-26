# coding=utf-8

"""
Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.seq = []

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        self.seq.append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        return word in self.seq

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for i in self.seq:
            if i.startswith(prefix):
                return True
        return False


if __name__ == '__main__':
    obj = Trie()
    obj.insert('word')
    param_2 = obj.search('word')
    print(param_2)
    param_3 = obj.startsWith('wo')
    print(param_3)