class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # global l
        # global w
        # global flag

        # if not board:
        #     return False

        # l = len(board)
        # w = len(board[0])

        # def backtrack(i,j,word):
        #     if word=="":
        #         return True

        #     if i not in range(0,l) or j not in range(0,w):
        #         return False

        #     if word[0]==board[i][j]:
        #         word=word[1:]
        #         return backtrack(i-1,j,word) or backtrack(i+1,j,word) or backtrack(i,j-1,word) or backtrack(i,j+1,word)

        #     print(word)
                
        
        # for i in range(l):
        #     for j in range(w):
        #         res = backtrack(i,j,word)
        #         if res:
        #             return res
        
        # return False

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False