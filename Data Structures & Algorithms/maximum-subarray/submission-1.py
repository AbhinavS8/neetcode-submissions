class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx = -float("inf")
        curmx = 0

        for i in nums:
            curmx += i
            
            mx = max(mx, curmx)

            if curmx<0:
                curmx=0
        
        return mx