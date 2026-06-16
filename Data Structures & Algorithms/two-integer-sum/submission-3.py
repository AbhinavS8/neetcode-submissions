class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        poses = {}
        for i in range(0,len(nums)):
            poses[nums[i]]=i
        
        for i in range(0,len(nums)):

            diff = target - nums[i]
            if diff in poses and i!=poses[diff]:
                return [i,poses[diff]]