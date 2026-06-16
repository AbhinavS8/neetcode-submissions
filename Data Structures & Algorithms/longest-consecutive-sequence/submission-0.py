class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        #hashing?
        longest=0
        for i in nums:
            c_max=0
            if (i-1) in hashset:
                continue
            
            while i in hashset:
                c_max+=1
                i=i+1
            
            longest=max(c_max,longest)

        return longest