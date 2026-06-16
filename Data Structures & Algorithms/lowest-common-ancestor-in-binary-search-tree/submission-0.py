# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # given all values are UNIQUE
        # first idea is bfs, since it goes level by level
        # have to find the elements also
        # just dfs down gang
        # KEEP TRACK OF PARENTS, return earliest common parent?
        # its a binary search tree!!!

        # stack = [root]
        # parents = []
        # paths = {}
        
        # foundp = False
        # foundq = False

        # while !(foundp and foundq):

        #     node = stack.pop()
        #     parents.append(node)

        #     if node.val == p:
        #         foundp = True
        #         paths['p']=parents.copy()

        # keep going! until value is outside range p-q
        # not outside range... if both are on one side or not!!


        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root





