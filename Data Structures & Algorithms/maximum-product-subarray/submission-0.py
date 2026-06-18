class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # dp = nums.copy()

        # def dfs(l,r):

        #     if l<0 or r>len(nums):
        #         return -1
            
        #     if r-l==1:
        #         return dp[l]
            
        res = nums[0]

        curmin, curmax = 1,1

        for num in nums:
            tmp = curmax * num
            curmax = max(num * curmax, num, num * curmin)
            curmin = min(tmp, num * curmin, num)
            res = max(res, curmax)

        return res