class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(grid, visited, row, col):
            visited[row][col] = True

            perimeter = 0

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1
                elif not visited[new_row][new_col]:
                    perimeter += dfs(grid, visited, new_row, new_col)
            
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid, visited, i, j)
        
        return 0