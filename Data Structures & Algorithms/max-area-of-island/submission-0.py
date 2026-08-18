class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        mx = 0
        rows = len(grid)
        cols = len(grid[0])

        def mark_visited(i, j):

            if not (0 <= i < rows and 0 <= j < cols):
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            area = 1

            area += mark_visited(i - 1, j)
            area += mark_visited(i + 1, j)
            area += mark_visited(i, j - 1)
            area += mark_visited(i, j + 1)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    mx = max(mx, mark_visited(i, j))

        return mx