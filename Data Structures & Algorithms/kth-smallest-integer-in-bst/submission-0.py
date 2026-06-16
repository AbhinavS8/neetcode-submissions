# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal? until kth element?

        stack = []
        curr = root
        cnt = 1

        while stack or curr:
            
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            if k==cnt:
                return curr.val
            cnt+=1
            curr = curr.right
