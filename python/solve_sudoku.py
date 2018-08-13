#!/usr/bin/env python3

def solve_sudoku(board):
    """
    Given a valid Sudoku board, solves it
    We keep track of a candidate dictionary for every cell and start by
    going thru every cell, and making modifying every row, col, and box
    affected by a (if-present) number in that cell. Then we use a queue
    to store cells with only 1 possible number that can be placed there, and
    proceed until a solution is produced. If a solution is not guaranteed,
    we can produce a check to see that all cells are filled in board (this
    is an in-place solution)

    The candidate dictionary is created for every cell. Depending on what
    you consider as N (we will consider N as the number of rows/cells since
    it is usually a square board), the space constraint is O(N^3).

    The algorithm is O(N^3) since we go thru every cell and modify constraints
    in a similar manner.

    A truly naive solution would go through all 9^81 possible Sudoku boards,
    but some of which are not valid, and see which one is the solution, This is
    O(N^83) which will never finish until the end of time, if ever
    """
    cands = [[{k: v for k, v in enumerate(range(1, 10))} for j in range(9)] for i in range(9)]

    # first pass
    q = []

    for row in range(9):
        for col in range(9):
            if board[row][col].isdigit():
                cands[row][col] = {}
                clear_row(cands, q, row, board[row][col])
                clear_col(cands, q, col, board[row][col])
                clear_box(cands, q, row, col, board[row][col])

    while len(q):
        current = q.pop()
        row, col = current[0], current[1]
        val = '.'
        for key in cand[row][col]:
            val = key
        cands[row][col] = {}
        clear_row(cands, q, row, val)
        clear_col(cands, q, col, val)
        clear_box(cands, q, row, col, val)

        # Finally fill in the value
        board[row][col] = val

def clear_row(cands, q, row, key):
    for col in range(len(cands[row])):
        cands[row][col].pop(key, None)
        if len(cands[row][col] == 1):
            q.append((row, col))

def clear_col(cands, q, col, key):
    for row in range(len(cands)):
        cands[row][col].pop(key, None)
        if len(cands[row][col] == 1):
            q.append((row, col))

def clear_box(cands, q, row, col, key):
    # determine box number
    box_row, box_col = row // 3, col // 3
    for i in range(box_row * 3, box_row * 3 + 2):
        for j in range(box_col * 3, box_col * 3 + 2):
            cands[i][j].pop(key, None)
            if len(cands[row][col] == 1):
                q.append((row, col))

