class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subbox = {}
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                row_val = board[i][j]
                col_val = board[j][i]
                # Check if row has duplicate values
                if row_val != ".":
                    if row_val in row_set:
                        return False
                    else:
                        row_set.add(row_val)

                # Check if column has duplicate values
                if col_val != ".":
                    if col_val in col_set:
                        return False
                    else:
                        col_set.add(col_val)

                        # Check if subbox has duplicate values
                r, c = i // 3, j // 3
                if row_val != ".":
                    if (r, c) in subbox:
                        if row_val in subbox.get((r, c)):
                            return False
                        else:
                            subbox.get((r, c)).add(row_val)
                    else:
                        subbox[(r, c)] = set(row_val)

        return True
