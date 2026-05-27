class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use hashmap to keep track of rows, columns and squares
        col_map = defaultdict(set)
        row_map = defaultdict(set)
        squ_map = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_num = board[i][j]
                if curr_num == ".":
                    continue

                curr_squ = 0
                if i > 5:
                    curr_squ += 6
                elif i > 2:
                    curr_squ += 3
                
                if j > 5:
                    curr_squ += 2
                elif j > 2:
                    curr_squ += 1

                if curr_num in col_map[j] or curr_num in row_map[i] or curr_num in squ_map[curr_squ]:
                    print(f"{i},{j} = {curr_num}")
                    return False
                
                row_map[i].add(curr_num)
                col_map[j].add(curr_num)
                squ_map[curr_squ].add(curr_num)

        return True