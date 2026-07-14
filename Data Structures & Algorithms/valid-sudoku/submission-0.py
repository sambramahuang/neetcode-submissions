class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        boxes = []

        for i in range(9):
            rows.append(set())
            columns.append(set())
            boxes.append(set())

        for r in range(9):
            for c in range(9):
                if board[r][c].isdigit():
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])

                    if board[r][c] in columns[c]:
                        return False
                    else:
                        columns[c].add(board[r][c])

                    if board[r][c] in boxes[(r//3)*3 + (c//3)]:
                        return False
                    else:
                        boxes[(r//3)*3 + (c//3)].add(board[r][c])
        
        return True
