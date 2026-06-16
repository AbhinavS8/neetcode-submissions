class TreeNode:
    def __init__(self,letter = "", isEnd = False):
        self.letter = letter
        self.isEnd = isEnd
        self.children = {}


class WordDictionary:

    def __init__(self, root = ""):
        self.root = TreeNode()  

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TreeNode(i)
                
            cur = cur.children[i]
        else:
            cur.isEnd = True

    def search(self, word: str) -> bool:
        
        # cur = self.root
        # flag = False

        # def dfs(node,word):
        #     nonlocal flag

        #     if word == "" and node.isEnd:
        #         flag = True
        #         return True
        #     elif word == "":
        #         return False

        #     i = word[0]
            

        #     if i == ".":
        #         for j in node.children:
        #             # print(i,word)
        #             dfs(node.children[j],word[1:])

        #     else:
        #         if i in node.children:
        #             # print("normal:",i,word)
        #             dfs(node.children[i],word[1:])
        #         else:
        #             return False

        
        # return flag
            
        def dfs(node, idx):
            if idx == len(word):
                return node.isEnd

            ch = word[idx]

            if ch == ".":
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(node.children[ch], idx + 1)

        cur = self.root
        return dfs(cur,0)

