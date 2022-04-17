# from datetime import time
from datetime import datetime
from typing import Optional


class SudokuSolver:
    def __init__(self, initial_board: list[list[int]]) -> 0:
        self.board = initial_board
        print('is valid', self.is_valid_board())
        self.counter = 0

    def is_possible(self, y: int, x: int, val: int) -> bool:
        for i in range(9):
            if self.board[y][i] == val:
                return False

        for i in range(9):
            if self.board[i][x] == val:
                return False

        min_y = y - (y % 3)
        min_x = x - (x % 3)

        for i in range(min_y, min_y + 3):
            for j in range(min_x, min_x + 3):
                if self.board[i][j] == val:
                    return False

        return True

    def is_valid_board(self) -> bool:
        clue_count = 0

        for y in range(9):
            for x in range(9):
                if self.board[y][x] != 0:
                    clue_count += 1

        print('clue count', clue_count)

        if clue_count < 17:
            return False

        for y in range(9):
            for x in range(9):
                if (val := self.board[y][x]) != 0:

                    for i in range(9):
                        if i != x and self.board[y][i] == val:
                            return False

                    for i in range(9):
                        if i != y and self.board[i][x] == val:
                            return False

                    min_y = y - (y % 3)
                    min_x = x - (x % 3)

                    for i in range(min_y, min_y + 3):
                        for j in range(min_x, min_x + 3):
                            if i != y and j != x and self.board[i][j] == val:
                                return False

        return True

    # possible next moves
    def solve_recursion(self) -> bool:
        self.counter += 1

        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    for val in range(1, 10):
                        if self.is_possible(y, x, val):
                            self.board[y][x] = val

                            # Prevent unnecessary iterations by not continuing
                            # if all values have been attempted
                            if self.solve_recursion():
                                return True

                            # Backtracking to remove incorrect solutions
                            self.board[y][x] = 0

                    # Return false if all values attempted on every 0 element
                    return False

        return True


# https://www.websudoku.com/?level=1&set_id=6303889381

easy = [[1, 8, 9, 0, 0, 5, 0, 3, 0],
        [5, 7, 0, 0, 0, 8, 4, 0, 0],
        [0, 2, 0, 9, 0, 0, 0, 0, 0],
        [6, 0, 0, 3, 0, 0, 1, 0, 0],
        [3, 1, 2, 0, 0, 0, 9, 6, 5],
        [0, 0, 8, 0, 0, 1, 0, 0, 2],
        [0, 0, 0, 0, 0, 7, 0, 9, 0],
        [0, 0, 1, 2, 0, 0, 0, 5, 6],
        [0, 9, 0, 8, 0, 0, 2, 4, 3]]

# https://www.websudoku.com/?level=4&set_id=4211215017

hard = [[0, 0, 0, 0, 0, 0, 8, 1, 0],
        [0, 3, 5, 2, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 3, 1, 0, 0, 6],
        [8, 0, 0, 0, 1, 5, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 9, 8, 0, 0, 0, 1],
        [3, 0, 0, 8, 2, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 6, 3, 7, 0],
        [0, 8, 4, 0, 0, 0, 0, 0, 0]]

test_1 = [[1, 0, 0, 0, 0, 7, 0, 9, 0],
          [0, 3, 0, 0, 2, 0, 0, 0, 8],
          [0, 0, 9, 6, 0, 0, 5, 0, 0],
          [0, 0, 5, 3, 0, 0, 9, 0, 0],
          [0, 1, 0, 0, 8, 0, 0, 0, 2],
          [6, 0, 0, 0, 0, 4, 0, 0, 0],
          [3, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 4, 0, 0, 0, 0, 0, 0, 7],
          [0, 0, 7, 0, 0, 0, 3, 0, 0]]

# use highest digits

test_2 = [[1, 0, 0, 2, 0, 0, 8, 9, 0],
          [0, 7, 8, 6, 0, 0, 0, 0, 0],
          [9, 0, 0, 0, 5, 7, 0, 0, 6],
          [8, 0, 0, 0, 3, 5, 9, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 7, 9, 4, 0, 0, 0, 8],
          [7, 0, 0, 8, 9, 0, 0, 0, 5],
          [0, 0, 0, 0, 0, 6, 7, 8, 0],
          [0, 8, 9, 0, 1, 0, 0, 0, 2]]

test_3 = [[5, 0, 0, 0, 0, 0, 0, 0, 3],
          [0, 2, 0, 0, 0, 0, 0, 0, 0],
          [7, 4, 0, 0, 8, 5, 1, 0, 2],
          [0, 8, 0, 0, 0, 4, 0, 0, 0],
          [0, 0, 0, 7, 2, 3, 0, 0, 0],
          [0, 0, 0, 6, 0, 0, 0, 4, 0],
          [9, 0, 5, 8, 1, 0, 0, 2, 7],
          [0, 0, 0, 0, 0, 0, 0, 8, 0],
          [6, 0, 0, 0, 0, 0, 0, 0, 9]]


# now think about the sudoku, what initial board would take your solution the longest time to solve it?
# what is the hardest test case for it?


def get_sudoku_time(board: list[list[Optional[int]]]) -> 0:
    solver = SudokuSolver(board)
    initial_time = datetime.now()
    solver.solve_recursion()
    print('timedelta', datetime.now() - initial_time)
    print('count', solver.counter)
    print('solution', solver.board)
    print('\n')


get_sudoku_time(easy)
get_sudoku_time(hard)
get_sudoku_time(test_1)
get_sudoku_time(test_2)
get_sudoku_time(test_3)
