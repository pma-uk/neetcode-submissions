class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        seen = set()
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs_traverse_island(x, y):
            if (x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == "0" or (x,y) in seen):
                return
            
            seen.add((x,y))

            dfs_traverse_island(x-1, y)
            dfs_traverse_island(x+1, y)
            dfs_traverse_island(x, y-1)
            dfs_traverse_island(x, y+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    count += 1
                    dfs_traverse_island(i, j)
        
        return count
