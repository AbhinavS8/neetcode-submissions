# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # first idea was to recurse,
        # maybe keep track of max and min so far?
        # its dfs based solution
        # okk hint said to update as we move down,
        # instead of as we move up as I thought
        # need a separate interval for each path?
        # 3-5-7  [3,5]

        def dfs(root,l,r):
            if not root:
                return True

            if root.val > l and root.val < r:

                return dfs(root.right,root.val,r) and dfs(root.left,l,root.val)

            else:
                return False
            
        return dfs(root,-1001,1001)
            

            