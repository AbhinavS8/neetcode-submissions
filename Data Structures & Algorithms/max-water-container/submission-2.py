class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l=0
        r=len(heights)-1
        maxw=0

        while r>l:
            if heights[l]>=heights[r]:
                maxw=max(maxw,(r-l)*heights[r])
                r-=1
            else:
                maxw=max(maxw,(r-l)*heights[l])
                l+=1
        return maxw
