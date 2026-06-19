class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # wordDict.sort(key=len, reverse=True)
        dp = list()
        dp = [0]*(len(s))
        dp.append(1)

        # def dfs(string):

        #     if string == "":
        #         return True
            
        #     for i in range(1,len(string)+1):
                
        #         # print(string[:i])
        #         if string[:i] in wordDict:
        #             if dfs(string[i:]):
        #                 return True
            
        #     else:
        #         return False

        def dfs(index):
            # print(dp)
            if dp[index]==1:
                return True
            
            if dp[index]==-1:
                return False

            for word in wordDict:
                if s[index: index+len(word)] == word:
                    if dfs(index + len(word)):
                        dp[index]=True
                        return True
                
            else:
                dp[index]=-1
                return False

        return dfs(0)

        # how to optimize runtime, what can I store?
        # memoization!!!