class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y, dist, seen):
            if (x not in range(rows) or y not in range(cols) or grid[x][y] < 0 or ((x,y) in seen and grid[x][y] <= dist)):
                return 

            if grid[x][y] > 0:
                grid[x][y] = min(dist, grid[x][y])
            
            seen.add((x,y))

            dfs(x, y-1, dist+1, seen)
            dfs(x, y+1, dist+1, seen)
            dfs(x-1, y, dist+1, seen)
            dfs(x+1, y, dist+1, seen)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs(i,j,0,set())

        return

            
