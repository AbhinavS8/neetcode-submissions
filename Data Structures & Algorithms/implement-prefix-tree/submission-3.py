class TreeNode:
    def __init__(self,letter = "", isEnd = False):
        self.letter = letter
        self.isEnd = isEnd
        self.children = {}

class PrefixTree:


        
    def __init__(self, root = ""):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TreeNode(i)
                
            cur = cur.children[i]
        else:
            cur.isEnd = True
            
                

    def search(self, word: str) -> bool:
        cur = self.root

        for i in word:
            if i not in cur.children:
                return False
            
            cur = cur.children[i]
        
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for i in prefix:
            if i not in cur.children:
                return False
            
            cur = cur.children[i]
        
        return True
        