class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,m=0,len(nums),0
        if r==0:
            if nums[0]==target:
                return 0
            else:
                return -1

        while r-l>0:
            if len(nums[l:r])==1:
                if nums[l]==target:
                    return l
                else:
                    return -1
            m=(r-l)//2+l
            if target<nums[m]:
                r=m
            elif target>nums[m]:
                l=m
            elif target==nums[m]:
                return m
        
        return -1
