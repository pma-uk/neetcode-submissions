class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Iterate over pacific border to get starting point
        # then use dfs to find all squares

        if not heights or not heights[0]:
            return [[]]

        pac, atl = set(), set()

        rows, cols = len(heights), len(heights[0])

        def dfs(x, y, currMax, seen):
            if (min(x,y) < 0 or x >= rows or y >= cols or heights[x][y] < currMax or (x,y) in seen):
                return

            seen.add((x,y))

            dfs(x, y-1, heights[x][y], seen)
            dfs(x, y+1, heights[x][y], seen)
            dfs(x-1, y, heights[x][y], seen)
            dfs(x+1, y, heights[x][y], seen)

        for i in range(rows):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, cols-1, heights[i][cols-1], atl)
            

        for j in range(cols):
            dfs(0, j, heights[0][j], pac)
            dfs(rows-1, j, heights[rows-1][j], atl)

        result = []

        for x, y in pac:
            if (x, y) in atl:
                result.append([x,y])

        return result

