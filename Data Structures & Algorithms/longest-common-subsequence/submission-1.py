class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[-1]*len(text1) for i in range(len(text2))]

        # def dfs(i,j):

        #     if i<0 or j<0:
        #         return 0
            
        #     if i==0 or j==0:
        #         if text1[j]==text2[i]:
        #             dp[i][j]=1
        #             return 1
                
        #         dp[i][j]=0
        #         return 0
            
        #     if dp[i-1][j]==-1:
        #         dp[i-1][j]=dfs(i-1,j)
            
        #     if dp[i][j-1]==-1:
        #         dp[i][j-1]=dfs(i,j-1)
            
        #     mx = max(dp[i][j-1],dp[i-1][j])

        #     if text1[j]==text2[i]:

        #         if dp[i-1][j-1]==-1:
        #             dp[i-1][j-1]=dfs(i-1,j-1)

        #         mx = max(1+dp[i-1][j-1],mx)
            
        #     return mx
        
        
        # res = dfs(len(text2)-1,len(text1)-1)
        # print(dp)
        # return res

        def dfs(i,j):

            if i<0 or j<0:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if text2[i]==text1[j]:
                res = 1+dfs(i-1,j-1)
            
            else:
                res = max(dfs(i-1,j),dfs(i,j-1))
            
            dp[i][j]=res
            return res
        
        return dfs(len(text2)-1,len(text1)-1)