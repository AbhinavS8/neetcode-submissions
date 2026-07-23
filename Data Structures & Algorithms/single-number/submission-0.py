class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        start = nums[0]

        for i in nums[1:]:
            start = start ^ i
        
        return start