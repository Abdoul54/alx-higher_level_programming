#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position
    for i in range(row):
        if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
            return False
    return True

def solve_nqueens(n):
    # Solve the N Queens problem using backtracking
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1)
    
    board = [-1] * n
    solutions = []
    backtrack(0)
    return solutions
