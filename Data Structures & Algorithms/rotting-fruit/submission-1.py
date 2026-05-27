class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        fresh = 0
        rotten = deque()

        def rotFruit(x, y):
            nonlocal fresh
            if (min(x,y) < 0 or x >= rows or y >= cols or grid[x][y] == 0 or grid[x][y] == 2):
                return
            
            # If fresh fruit found, rot it, and remove from fresh set
            if grid[x][y] == 1:
                fresh -= 1
                rotten.append((x,y))
                grid[x][y] = 2

        # Find fresh and rotten fruit 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))

        # If no fresh fruit, already at state
        if fresh == 0:
            return 0

        dist = -1

        # Rot fruit radiating out from currently found fruit
        while rotten:
            # Current radius of dist
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                rotFruit(x, y-1)
                rotFruit(x, y+1)
                rotFruit(x-1, y)
                rotFruit(x+1, y)
            
            dist += 1

        # If fresh fruit remaining, impossible to rot all fruit
        if fresh > 0:
            return -1

        return dist