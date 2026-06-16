# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # so need to start checking only if first val matches
        # if it does, traverse in that order separately?
        # and then come back to the original?
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val==subRoot.val:
                if self.isSameTree(node,subRoot):
                    return True

            if node.left:
                stack.append(node.left)          
            if node.right:
                stack.append(node.right)

        
        return False


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        else:
            return False