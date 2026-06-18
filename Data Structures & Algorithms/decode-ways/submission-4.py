# class Solution:
#     def numDecodings(self, s: str) -> int:
        
#         cnt = 0
#         if len(s)==0:
#             return 0
        
#         if s[0]=='0':
#             return 0

#         for i in range(len(s)):

#             if i==0:
#                 cnt+=1
#                 continue
            
#             # zero condition

#             if s[i]=='0':
#                 pass

#             # multiply condition    
#             elif s[i-1]=='1':

#                 if i-2>=0 and s[i-2] in ("1","2"):
#                     cnt+=1

#                 cnt+=1
            
#             elif s[i-1]=='2' and int(s[i]) in range(7):
#                 cnt+=1


#                 if i-2>=0 and s[i-2] in ("1","2"):
#                     cnt+=1
            

#         return cnt

class Solution:
    def numDecodings(self, s: str) -> int:
        
        # dfs(i) is value of decodings for substring [i:]
        dp = {}
        dp[len(s)]=1

        def dfs(i):

            if i in dp:
                return dp[i]

            if s[i]=="0":
                return 0
            
            res = dfs(i+1)
            if i < len(s) -1:
                if s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456"):
                    
                    res+=dfs(i+2)
            dp[i] = res
            return res
        
        return dfs(0)

