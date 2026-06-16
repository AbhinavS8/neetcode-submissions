class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 3
        
        
        # n = 4, 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
        # n = 5, 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+2+1, 2+1+2, 1+2+2
        # order matters
        prev = 1
        cur = 2
        temp = 0
        for i in range(2,n):
            temp = prev
            prev = cur
            cur = temp+prev
        
        return cur