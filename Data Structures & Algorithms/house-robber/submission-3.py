# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         # max(odd indexes so far, even indexes so far) NOT LIKE THIS
#         # [0,3,0,1,1000]
#         # [2,9,8,3,6]
        
#         ls = [0]*len(nums)
            
#             if len(nums)-index <= 0:
#                 return 0
            
#             ls[index] = max(nums[index] + ls(index+2), ls(index+1))

#         return dfs(0)

#         # if len(nums)==1:
#         #     return nums[0]

#         # for i in range(0,len(nums)):

#         #     if i==0 or i==1:
#         #         continue
#         #     print(nums)
#         #     nums[i] = max(nums[i]+nums[i-2],nums[i-1])
#         #     print(nums)
        
#         # return nums[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]