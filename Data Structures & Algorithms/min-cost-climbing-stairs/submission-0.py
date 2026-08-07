class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # can go from either last or second last
        # at each step can move one or two indexes


        if len(cost)==1:
            return cost[0]

        if len(cost)==2:
            return min(cost[0],cost[1])

        dp = [-1]*len(cost)

        
        def recurse(index):
            
            if index == len(cost)-2 or index == len(cost)-1:
                dp[index]=cost[index]
                return cost[index]

            if dp[index]!=-1:
                return dp[index]
            
            
            dp[index] = cost[index]+min(recurse(index+1),recurse(index+2))
            return dp[index]
        
        recurse(0)
        return min(dp[0],dp[1])
