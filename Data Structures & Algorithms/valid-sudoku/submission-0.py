class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 rows, 9 columns, 9 squares
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                # check if in current row, col or square
                currSquare = (i // 3) * 3 + (j // 3) # top down squares increment in 3s, left to right in 1s
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[currSquare]:
                    print(f"{i} and {j}")
                    return False

                # add to sets
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[currSquare].add(board[i][j])

        return True
                