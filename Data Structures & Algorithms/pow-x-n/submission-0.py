class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1

        num=1

        if n>0:
            for i in range(n):
                num=x*num
        
        else:
            for i in range(-n):
                num=num/x
        return num