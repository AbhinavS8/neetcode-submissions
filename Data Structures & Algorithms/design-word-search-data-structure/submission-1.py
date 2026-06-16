class TreeNode:
    def __init__(self,letter = "", isEnd = False):
        self.letter = letter
        self.isEnd = isEnd
        self.children = {}

# path = []
        # cur = self.root
        
        # need to check all possible routes
        # multiple pathing thingies may be there
        # bl..d
        # just push to stack each time a dot appears?
        # [o], [o,l] 
        # []
     
# flag = False
#         cur = self.root

#         def dfs(root,word):
#             nonlocal cur
            
#             print(word)
#             if word == "":
#                 flag = True
#                 return True

#             for i in word:
#                 if not cur.children:
#                     return False

#                 if i != '.':
#                     if i in cur.children:
#                         cur = cur.children[i]
#                     else:
#                         return False
#                 else:
#                     for i in cur.children:
#                         dfs(root,word[1:]) 
        
        
#         dfs(cur,word)
#         return flag
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
        
        cur = self.root
        flag = False

        def dfs(node,word):
            nonlocal flag

            if word == "" and node.isEnd:
                flag = True
                return True
            elif word == "":
                return False
                
            i = word[0]
            

            if i == ".":
                for j in node.children:
                    # print(i,word)
                    dfs(node.children[j],word[1:])

            else:
                if i in node.children:
                    # print("normal:",i,word)
                    dfs(node.children[i],word[1:])
                else:
                    return False

        dfs(cur,word)
        return flag
            


