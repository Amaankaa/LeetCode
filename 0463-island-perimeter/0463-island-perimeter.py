class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs_itr(start_row, start_col):
            stack = [(start_row, start_col)]
            visited[start_row][start_col] = True
            perimeter = 0

            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if not inbound(new_row, new_col) or grid[new_row][new_col]==0:
                        perimeter += 1
                    elif not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        stack.append((new_row, new_col))
            
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs_itr(i, j)
        
        return 0