class Solution:
    def isHappy(self, n: int) -> bool:
        
        sm = 0
        ls = []

        while True:
            sm=0
            for i in str(n):
                sm += int(i)**2

            if sm==1:
                return True

            if sm in ls:
                return False
            
            ls.append(sm)
            # print(ls)

            n=sm