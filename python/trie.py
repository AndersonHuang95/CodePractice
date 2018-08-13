class TrieNode: 
    def __init__(self, value=None, children=None, is_word=False): 
        self.value = value if value else ""
        self.children = children if children else {}
        self.is_word = is_word
    
    def add_child(self, child):
        """
        Args:
            child (string) 
        Returns: 
            void - adds child to children set
        """
        self.children[child] = TrieNode(child)
    
    def has_child(self, child):
        return child in self.children
        
    def get_is_word(self):
        return self.is_word
    
    def set_is_word(self, is_word):
        self.is_word = is_word

class Trie:
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root 
        for letter in word: 
            if not current.has_child(letter):
                current.add_child(letter)
            current = current.children[letter]
        current.set_is_word(True)
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word: 
            if not current.has_child(letter): 
                return False
            else:
                current = current.children[letter]
        return current.get_is_word()
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix: 
            if not current.has_child(letter):
                return False
            else:
                current = current.children[letter]
        return True
        
def main(): 
    trie = Trie()
    trie.insert("add")
    trie.insert("adderall")
    trie.insert("orange")
    assert trie.startsWith("adde") == True
    assert trie.search("adderall") == True
    assert trie.startsWith("ore") == False

    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app");   
    assert trie.search("app") == True

if __name__ == '__main__':
    main()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)