class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i=0
        power=0

        while i<(len(nums)-1):
            
            power-=1

            if nums[i]==0 and power<=0:
                return False
            
            power = max(nums[i],power)
            i+=1
        
        if i>=len(nums)-1:
            return True
        
        return False