class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        l = len(heights)
        r = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i,j,ocean,prev):
            
            if 0<=i<l and 0<=j<r:

                if prev <= heights[i][j]:

                    if ocean=="p":
                        
                        if (i,j) not in pacific:
                            pacific.add((i,j))
                            dfs(i-1,j,ocean,heights[i][j])
                            dfs(i+1,j,ocean,heights[i][j])
                            dfs(i,j-1,ocean,heights[i][j])
                            dfs(i,j+1,ocean,heights[i][j])

                    else:
                        if (i,j) not in atlantic:
                            atlantic.add((i,j))
                            dfs(i-1,j,ocean,heights[i][j])
                            dfs(i+1,j,ocean,heights[i][j])
                            dfs(i,j-1,ocean,heights[i][j])
                            dfs(i,j+1,ocean,heights[i][j])
                        
        for i in range(l):
            p = (i,0)
            a = (i,r-1)

            dfs(i,0,"p",-1)
            dfs(i,r-1,"a",-1)

        for i in range(r):
            p = (0,i)
            a = (l-1,i)

            dfs(0,i,"p",-1)
            dfs(l-1,i,"a",-1)

        res=[]
        print(pacific,atlantic)
        for i in pacific:
            if i in atlantic:
                res.append(list(i)) 

        return res
