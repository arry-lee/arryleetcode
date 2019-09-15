#ÊµÏÖTrie(Ç°×ºÊ÷)
#2019-08-17 15:12:05

class Node:
    def __init__(self,is_word=False):
        self.is_word = is_word
        self.next = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self._root
        for w in word:
            if cur.next.get(w,None) is None:
                cur.next[w] = Node()
            cur = cur.next[w]
        cur.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self._root
        for w in word:
            if cur.next.get(w,None) is None:
                return False
            cur = cur.next[w]
              
        return cur.is_word
       
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self._root
        for w in prefix:
            if cur.next.get(w,None) is None:
                return False
            cur = cur.next[w]
              
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)