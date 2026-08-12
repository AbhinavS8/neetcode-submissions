# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # return cur and max so far?
        def recurse(node):

            if node == None:
                return [-1,-2]
            
            l = recurse(node.left)
            r = recurse(node.right)
            
            cur = 1+max(l[0],r[0])
            mx = max(2+l[0]+r[0],r[1],l[1])

            print("NODE",node.val,"OTHER SHI",cur,mx)
            return [cur,mx]

        res = recurse(root)
        return max(res[0],res[1])
