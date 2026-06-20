class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*n for i in range(m)]

        def dfs(i,j):
            
            if i==0 or j==0:
                dp[i][j]=1
                return 1
            
            if dp[i][j]==0:
                dp[i][j] = dfs(i-1,j)+dfs(i,j-1)
                
            return dp[i][j]

        return dfs(m-1,n-1)

        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j==0:
        #             dp[i][j]=1
                 
        print(dp)
