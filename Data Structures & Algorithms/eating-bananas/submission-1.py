class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        l=1
        r=max(piles)
        f=r

        while r>=l:
            k=(l+r)//2

            time=0

            for i in piles:
                time+= math.ceil(int(i)/k)
            
            if time<=h:
                f=k
                r=k-1
            else:
                l=k+1
        
        return f
