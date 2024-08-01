#!/usr/bin/python3

"""
Implementation of the N-Queens problem
"""

import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Recursive backtracking function to solve N-Queens
    Args:
        r (int): the current row being processed
        n (int): total number of queens
        cols (set): columns occupied by queens
        pos (set): positive diagonals occupied by queens
        neg (set): negative diagonals occupied by queens
        board (list): representation of the chessboard
    Returns:
        None
    """
    if r == n:
        solution = []
        for i in range(len(board)):
            for k in range(len(board[i])):
                if board[i][k] == 1:
                    solution.append([i, k])
        # Output the queen positions
        print(solution)
        return

    for c in range(n):
        # Skip if the column or either diagonal is under attack
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place the queen on the board
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Recurse to the next row
        backtrack(r+1, n, cols, pos, neg, board)

        # Remove the queen to backtrack
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solve the N-Queens problem
    Args:
        n (int): number of queens. Must be >= 4
    Returns:
        None
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
