# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         if not grid:
#             return 0

#         l = len(grid)
#         r = len(grid[0])

#         def mark_visited(i,j):

#             if 0<= i <l and 0<= j <r:
#                 if grid[i][j]=="1":
#                     grid[i][j]="0"
#                     mark_visited(i-1,j)
#                     mark_visited(i+1,j)
#                     mark_visited(i,j-1)
#                     mark_visited(i,j+1)
#         tot = 0

#         for i in range(l):
#             for j in range(r):
#                 if grid[i][j]=="1":
#                     tot+=1
#                     mark_visited(i,j)

#         return tot

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands