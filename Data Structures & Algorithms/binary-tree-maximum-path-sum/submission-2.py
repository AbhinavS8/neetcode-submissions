# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # sum up the children, take max
        
        
        
        # first issue, need to return 0 if the value of child is negative
        # second issue, should not update max if its less, need to keep track of two things?
        # no, they wouldnt ask something like that
        # THEY ASKED SOMETHING LIKE THAT
        # keep track of global as well. damn. and had to use helper func

        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]   
