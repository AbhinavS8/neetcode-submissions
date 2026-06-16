class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        l = len(grid)
        r = len(grid[0])

        def mark_visited(i,j):

            if 0<= i <l and 0<= j <r:
                if grid[i][j]=="1":
                    grid[i][j]="0"
                    mark_visited(i-1,j)
                    mark_visited(i+1,j)
                    mark_visited(i,j-1)
                    mark_visited(i,j+1)
        tot = 0

        for i in range(l):
            for j in range(r):
                if grid[i][j]=="1":
                    tot+=1
                    mark_visited(i,j)

        return tot