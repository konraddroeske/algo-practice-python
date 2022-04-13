import copy
from collections import defaultdict
from typing import Optional


class SudokuSolver:
    def __init__(self, initial_board: list[list[Optional[int]]]) -> None:
        self.board = initial_board
        self.counter = 0

    def is_possible(self, y: int, x: int, val: Optional[int]) -> bool:
        # print('check row if it contains number')
        for i in range(9):
            if self.board[y][i] == val:
                return False

        # print('check col if it contains number')
        for i in range(9):
            if self.board[i][x] == val:
                return False

        # print('find box and check if it contains number')
        min_y = y - (y % 3)
        min_x = x - (x % 3)

        for i in range(min_y, min_y + 3):
            for j in range(min_x, min_x + 3):
                if self.board[i][j] == val:
                    return False

        return True

    # possible next moves
    def solve_recursion(self) -> bool:
        self.counter += 1

        for y in range(9):
            for x in range(9):
                if self.board[y][x] is None:
                    for val in range(1, 10):
                        if self.is_possible(y, x, val):
                            self.board[y][x] = val

                            # Prevent unnecessary iterations by not continuing
                            # if all values have been attempted
                            if self.solve_recursion():
                                return True

                            # Backtracking to remove incorrect solutions
                            self.board[y][x] = None

                    # Return false if all values attempted on every None element
                    return False

        return True


# https://www.websudoku.com/?level=1&set_id=6303889381

board = [[1, 8, 9, None, None, 5, None, 3, None],
         [5, 7, None, None, None, 8, 4, None, None],
         [None, 2, None, 9, None, None, None, None, None],
         [6, None, None, 3, None, None, 1, None, None],
         [3, 1, 2, None, None, None, 9, 6, 5],
         [None, None, 8, None, None, 1, None, None, 2],
         [None, None, None, None, None, 7, None, 9, None],
         [None, None, 1, 2, None, None, None, 5, 6],
         [None, 9, None, 8, None, None, 2, 4, 3]]

solver = SudokuSolver(board)
solver.solve_recursion()
print('final board', solver.board)
print('final count', solver.counter)
