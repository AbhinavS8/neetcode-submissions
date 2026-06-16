class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # poses = {}
        # for i in range(0,len(nums)):
        #     poses[nums[i]]=i
        
        # for i in range(0,len(nums)):

        #     diff = target - nums[i]
        #     if diff in poses and i!=poses[diff]:
        #         return [i,poses[diff]]

        poses = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in poses:
                return [poses[diff],i]
            else:
                poses[n]=i
