# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # use bfs, queue?
        # [1] [2,3] 


        if not root:
            return []

        q = deque([root])

        levels = list()

        while q:
            level = []
            for i in range(0,len(q)):

                node = q.popleft()
                level.append(node.val)

                print(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                
            levels.append(level)

        return levels