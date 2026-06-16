class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h=len(grid)
        w=len(grid[0])

        # newmap=[[0]*w]*h
        cnt=0

        def recurse(i,j,h,w):

            if i==-1 or i==h:
                return 0
            
            if j==-1 or j==w:
                return 0
            
            if grid[i][j]!="1":
                return 0
            else:
                grid[i][j]="-1"
                recurse(i+1,j,h,w)
                recurse(i,j+1,h,w)
                recurse(i-1,j,h,w)
                recurse(i,j-1,h,w)

        for i in range(0,h):
            for j in range(0,w):
                if grid[i][j]=="1":
                    recurse(i,j,h,w)
                    cnt+=1
        
        return cnt
                