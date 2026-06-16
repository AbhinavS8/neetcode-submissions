class Solution:
    def findMin(self, nums: List[int]) -> int:
        #SEARCH FOR THE ENDPOINT DUMMY
        #but which side to go down?

        #[1,2,3,4,5]
        #[5,1,2,3,4]
        #[4,5,1,2,3]
        #[3,4,5,1,2]
        #[2,3,4,5,1]
        
        l=0
        r=len(nums)
        if r==1:
            return nums[0]

        while l<=r:
            print(l,r)
            if r-l==1:
                return nums[l]
            
            if r-l==2:
                if nums[l]<nums[r-1]:
                    return nums[l] 
                else:
                    return nums[r-1]

            m=(l+r)//2

            # if nums[m-1]>nums[m] and nums[m+1]>nums[m]:
            #     return nums[m]
            # elif nums[m-1]<nums[m]:
            #     l=m+1
            # elif nums[m+1]

            if nums[m]>nums[l] and nums[m]>nums[r-1]:
                l=m+1
            else:
                r=m+1
        
        return nums[l]


        
