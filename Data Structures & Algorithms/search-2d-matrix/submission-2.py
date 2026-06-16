class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            rowMid = (l + r) // 2

            curr = matrix[rowMid][0]

            if target > curr:
                l = rowMid + 1
            elif target < curr:
                r = rowMid - 1
            else:
                return True

        ## Target not found, but current 'r' indicates current row to search
        searchRow = r
        
        l, r = 1, len(matrix[searchRow])

        if searchRow < 0 or matrix[searchRow][0] > target or matrix[searchRow][-1] < target:
            return False

        while l <= r:
            colMid = (l + r) // 2

            curr = matrix[searchRow][colMid]

            if target > curr:
                l = colMid + 1
            elif target < curr:
                r = colMid - 1
            else:
                return True

        return False