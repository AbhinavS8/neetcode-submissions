class Solution:
    def numDecodings(self, s: str) -> int:
        
        prev2 = 1  # dp[0]

        prev1 = 0 if s[0] == '0' else 1

        for i in range(1, len(s)):
            cur = 0

            if s[i] != '0':
                cur += prev1

            if 10 <= int(s[i-1:i+1]) <= 26:
                cur += prev2

            prev2, prev1 = prev1, cur

        return prev1


# # class Solution:
# #     def numDecodings(self, s: str) -> int:
        
# #         # dfs(i) is value of decodings for substring [i:]
# #         dp = {}
# #         dp[len(s)]=1

# #         def dfs(i):

# #             if i in dp:
# #                 return dp[i]

# #             if s[i]=="0":
# #                 return 0
            
# #             res = dfs(i+1)
# #             if i < len(s) -1:
# #                 if s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456"):
                    
# #                     res+=dfs(i+2)
# #             dp[i] = res
# #             return res
        
# #         return dfs(0)

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         #space optimized
#         dp = dp2 = 0
#         dp1 = 1
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == "0":
#                 dp = 0
#             else:
#                 dp = dp1

#             if i + 1 < len(s) and (s[i] == "1" or
#                s[i] == "2" and s[i + 1] in "0123456"
#             ):
#                 dp += dp2
#             dp, dp1, dp2 = 0, dp, dp1
#         return dp1
