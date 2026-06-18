class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {i:-1 for i in range(amount)}

        if amount==0:
            return 0
        
        for i in coins:
            dp[i-1]=1

        for cursum in range(amount):
            # print(dp)
            minval = float("inf")

            if cursum+1 in coins:
                continue

            for coinval in coins:

                if cursum - coinval in dp:

                    prev = cursum-coinval
                    if dp[prev]!=-1:
                        minval = min(minval,dp[prev]+1)
                    
            dp[cursum] = minval
        
        if dp[amount-1]==float("inf"):
            return -1

        return dp[amount-1]
        
        
