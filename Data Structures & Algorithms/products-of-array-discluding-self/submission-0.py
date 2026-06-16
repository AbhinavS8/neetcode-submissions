class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #easy approacch - multiply everything and divide

        #forward pass
        #[1,1,2,8]
        #backward pass
        #[48,24,6,1]
        le=len(nums)
        fwlist=[1]*le
        bklist=[1]*le    

        for i in range(1,le):
            fwlist[i]=nums[i-1]*fwlist[i-1]

        for i in range(le-2,-1,-1):
            bklist[i]=nums[i+1]*bklist[i+1]


        return [fwlist[i]*bklist[i] for i in range(0,len(nums))]

