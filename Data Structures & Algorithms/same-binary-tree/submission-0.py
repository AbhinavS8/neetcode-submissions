# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # need to check all nodes in order, while also avoid null issues

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        else:
            return False

        
    
    # def printInorder(self, root):
    #     if root:
    #         # Traverse left subtree
    #         self.printInorder(root.left)
            
    #         # Visit node
    #         print(root.val,end=" ")
            
    #         # Traverse right subtree
    #         self.printInorder(root.right)
        
    

