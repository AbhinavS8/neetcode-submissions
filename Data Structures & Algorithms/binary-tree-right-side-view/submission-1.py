# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # at each level, rightmost node.
        # BFS?
        # add elems to queue
        # in each level, only print rightmost, then traverse down
        # to next level
        # how to verify if on same level??
        # add to new queue instead of same, then copy I guess
        if root == None:
            return []
            
        cur = deque([root])
        nxt_level = deque()
        res = []
        while len(cur) != 0:
            nxt_level.clear()

            for i in range(len(cur)):
                n = cur.popleft()
                
                if n.left != None:
                    nxt_level.append(n.left)    
                
                if n.right != None:
                    nxt_level.append(n.right)

                # print([i.val for i in cur],[i.val for i in nxt_level])
            res.append(n.val)            
            cur = nxt_level.copy()

        return res