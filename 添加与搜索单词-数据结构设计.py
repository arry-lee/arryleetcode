#添加与搜索单词-数据结构设计
#2019-08-17 15:57:53

class Node:
    def __init__(self,is_word=False):
        self.is_word = is_word
        self.next = dict()

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self._root
        for w in word:
            if cur.next.get(w,None) is None:
                cur.next[w] = Node()
            cur = cur.next[w]
        cur.is_word = True        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_RE(root,word):
            cur = root
            if not word:
                return cur.is_word
            if len(word) == 1:
                if word != '.':
                    return cur.next.get(word,None) and cur.next[word].is_word
                else:
                    return any(cur.next[k].is_word for k in cur.next)
            
            if word[0]!=".":
                if cur.next.get(word[0],None) is None:
                    return False
                else:
                    return search_RE(cur.next[word[0]],word[1:])
            else:
                return any(search_RE(cur.next[k],word[1:]) for k in cur.next)
            
        return search_RE(self._root,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)