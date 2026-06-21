class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        sm = n * (n+1) //2

        for i in nums:
            sm -= i
        
        return sm