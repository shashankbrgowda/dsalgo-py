import collections
from typing import List


class ValidSudoku:
    def valid_sudoku(self, board: List[List[str]]):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                    print("Not a valid sudoku")
                    return
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)

        print("Its a valid Sudoku")


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    vs = ValidSudoku()
    vs.valid_sudoku(board)
