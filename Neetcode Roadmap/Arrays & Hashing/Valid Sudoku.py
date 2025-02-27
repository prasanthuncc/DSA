"""
Valid Sudoku
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.


"""
from collections import defaultdict
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    columns = defaultdict(set)
    block = defaultdict(set)
    for r in range(len(board)):
        for c in range(len(board[r])):
            val = board[r][c]
            if val == ".":
                continue
            elif val in rows[r] or val in columns[c] or val in block[(r // 3, c // 3)]:
                return False
            else:
                rows[r].add(val)
                columns[c].add(val)
                block[(r // 3, c // 3)].add(val)
    return True


if __name__ == '__main__':
    print(isValidSudoku(board=
                        [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", ".", ".", ".", ".", ".", "2", ".", "."],
                         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(isValidSudoku(board=
                        [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                         [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", ".", ".", ".", ".", ".", "2", ".", "."],
                         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."],
                         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."],
                         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
