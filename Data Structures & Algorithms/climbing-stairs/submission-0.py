class Solution:
    def climbStairs(self, n: int) -> int:
        
        #1 - 1   -1
        #2 - 1+1 2   -2
        #3 - 1+1+1 1+2 2+1   -3
        #4 - 1+1+1+1 2+1+1 1+2+1 1+1+2 2+2   -5
        #5 - 1+1+1+1+1 2+1+1+1 1+2+1+1 1+1+2+1 1+1+1+2 2+2+1 2+1+2 1+2+2 - 8
        #fibonaccciiiii
        prev=1
        curr=1
        for i in range(1,n):
            temp=curr
            curr=curr+prev
            prev=temp
            
        return curr