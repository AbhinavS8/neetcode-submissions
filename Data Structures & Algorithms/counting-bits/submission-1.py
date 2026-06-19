# class Solution:
#     def countBits(self, n: int) -> List[int]:
        
#         output = []
#         for i in range(n+1):
            
#             cnt = 0
#             for j in range(32):
#                 cnt += i & 1
#                 i = i >> 1
            
#             output.append(cnt)
        
#         return output

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp