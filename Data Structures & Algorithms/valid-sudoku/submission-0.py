class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

        for j in range(len(board[0])):
            column = set()
            for i in range(len(board)):
                board[i][j]
                if board[i][j] != '.':
                    if board[i][j] in column:
                        return False
                    column.add(board[i][j])

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        board[row + i][col + j]
                        if board[row + i][col + j] != '.':
                            if board[row + i][col + j] in box_set:
                                return False
                            box_set.add(board[row + i][col + j])

        return True