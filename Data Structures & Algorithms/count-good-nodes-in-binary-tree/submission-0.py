# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def recurse(node, maxseen):

            # 
            if node == None:
                return 0

            l = 0
            if node.val >= maxseen:

                maxseen = node.val
                l+=1

            return l + recurse(node.left,maxseen) + recurse(node.right,maxseen) 

        return recurse(root,-101)            