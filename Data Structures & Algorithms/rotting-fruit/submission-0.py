class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        fresh = set()
        rotten = deque()
        seen = set()

        def rotFruit(x, y):
            if (min(x,y) < 0 or x >= rows or y >= cols or grid[x][y] == 0 or (x,y) in seen):
                return
            
            # If fresh fruit found, rot it, and remove from fresh set
            if grid[x][y] == 1:
                fresh.remove((x,y))
                rotten.append((x,y))

            seen.add((x,y))

        # Find fresh and rotten fruit 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.append((i,j))
                    seen.add((i,j))

        # If no fresh fruit, already at state
        if not fresh:
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
        if fresh:
            return -1

        return dist