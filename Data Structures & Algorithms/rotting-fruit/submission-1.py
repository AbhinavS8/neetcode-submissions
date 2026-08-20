from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # find max depth of fresh fruit from a rotten fruit using BFS 
        # if it doesn't expand anything at all, return -1

        q = deque()
        depth = 0

        def expand(i,j):

            if not (0 <= i < len(grid) and 0<= j < len(grid[0])):
                return
            
            if grid[i][j]!=1:
                return
            
            grid[i][j]=2
            q.append((i,j))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
        
        while q:
            # print(q)
            for i in range(len(q)):
                n = q.popleft()
                expand(n[0]-1,n[1])
                expand(n[0]+1,n[1])
                expand(n[0],n[1]-1)
                expand(n[0],n[1]+1)

            # print(q)
            if not q:
                break
            depth += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1

        return depth