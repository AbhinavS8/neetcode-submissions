# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
        
#         # should I dfs or bfs?? hmmmmm
#         # check if any of the O nodes are connected to outside grid
#         # if you find an escape/edge route, return it and stop execution
#         # is it better to mark as visited/safe and then run it back?
#         # probably uses less memory

#         # def slaughter_ogroups(i,j):

#         #     if not (0 <= i < len(board) and 0 <= j < len(board[0])):
#         #         return 
            
#         #     if grid[i][j]=="X":
#         #         return
                        

#         # first explore, while marking as intermediate state
#         # if you encounter an edge, leave as intermediate/visited
#         # if fully explored, return True, if all true, mark as X

#         def explore(i,j):

#             if not (0 <= i < len(board) and 0 <= j < len(board[0])):
#                 return True
            
#             if board[i][j]=="X":
#                 return False
            
#             if board[i][j]=="-":
#                 return False
            
#             board[i][j]='-'
#             return explore(i-1,j) or explore(i+1,j) or explore(i,j-1) or explore(i,j+1) 

            

#         def slaughter_os(i,j):

#             if not (0 <= i < len(board) and 0 <= j < len(board[0])):
#                 return
            
#             if board[i][j]=="X":
#                 return
            
#             board[i][j] = "X"
#             slaughter_os(i-1,j)
#             slaughter_os(i+1,j)
#             slaughter_os(i,j-1)
#             slaughter_os(i,j+1)

#         for i in range(len(board)):
#             for j in range(len(board[0])):

#                 if board[i][j]=="O":

#                     if not explore(i,j):
#                         slaughter_os(i,j)
                
#                 # if board[i][j]=="-":

#                 #     board[i][j]="O"
#                 # print(board)
#         for i in range(len(board)):
#             for j in range(len(board[0])):

#                 if board[i][j]=="-":

#                     board[i][j]="O"
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == 0 or r == ROWS - 1 or
                        c == 0 or c == COLS - 1) and board[r][c] == "O":
                        q.append((r, c))
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            q.append((nr, nc))

        capture()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"