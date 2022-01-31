class TrieNode:
    def __init__(self, char='/0'):
        self.char = char
        self.end = False
        self.next_char = [None] * 26
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if not curr.next_char[ord(word[i])-ord('a')]:
                curr.next_char[ord(word[i])-ord('a')] = TrieNode(word[i])    
            curr = curr.next_char[ord(word[i])-ord('a')]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if not curr.next_char[ord(word[i])-ord('a')]:
                return False
            curr = curr.next_char[ord(word[i])-ord('a')]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if not curr.next_char[ord(prefix[i])-ord('a')]:
                return False
            curr = curr.next_char[ord(prefix[i])-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)