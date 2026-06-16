"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
#         if not node:
#             return None
        
        # input is just the first node. we have to construct separately
        # at each node, mark as visited andgo to all its neighbors
        # (create new node if it doesn't exist)
        # add everything to neighbors list and continue to any unexplored node

        # implementation notes:
        # recursively visit nodes? global visited set?

        # visited = set()

        # def recurse(node):
        #     if node in visited:
        #         return None

        #     visited.add(node)

            
            
        #     for i in visited:
        #         print(i.val, end="/")
            
        #     for i in node.neighbors:
        #         print(node.val,i.val)
        #         recurse(i)
        #     newnode = Node(node.val)
        #     newnode.neighbors = node.neighbors.copy()

        #     return newnode
        # return recurse(node)
        


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None



             