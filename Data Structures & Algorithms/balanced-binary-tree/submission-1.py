# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recurse(node):

            if node == None:
                return 0

            
            l = recurse(node.left)
            r = recurse(node.right)
            
            if l==-1 or r==-1:
                return -1
            
            l+=1
            r+=1

            # print("node:",node.val,"vals:",l,r)

            if abs(l-r) > 1:
                return -1

            return max(l,r)

        if recurse(root)!=-1:
            return True
        else:
            return False