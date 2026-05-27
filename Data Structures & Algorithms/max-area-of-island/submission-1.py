class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        maxArea = 0
        seen = set()

        rows, cols = len(grid), len(grid[0])

        def dfs_traverse_island(x, y):
            if (x not in range(rows) or y not in range(cols) or grid[x][y] == 0 or (x,y) in seen):
                return 0

            seen.add((x,y))

            return 1 + dfs_traverse_island(x,y-1) + dfs_traverse_island(x,y+1) + dfs_traverse_island(x-1,y) + dfs_traverse_island(x+1,y)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in seen:
                    maxArea = max(maxArea, dfs_traverse_island(i,j))
        
        return maxArea
