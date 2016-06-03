from itertools import permutations

# 6 line solution? Investigate this
# def board(vec):
#     '''Translate column positions to an equivalent chess board.
#
#     >>> board([0, 4, 7, 5, 2, 6, 1, 3])
#     Q-------
#     ----Q---
#     -------Q
#     -----Q--
#     --Q-----
#     ------Q-
#     -Q------
#     ---Q----
#
#     '''
#
#     for col in vec:
#         s = ['-'] * len(vec)
#         s[col] = 'Q'
#         print ''.join(s)
#     print
#
# def solve(n):
#     cols = range(n)
#     for vec in permutations(cols):
#         if (n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols))):
#             print board(vec)
#
# solve(8)



BOARD_SIZE = 8

def safe(col, queens):
    row = len(queens)+1
    for queen in queens:
        r,c = queen
        if r == row: return False # Check row
        if c == col: return False # Check column
        if (col-c) == (row-r): return False # Check left diagonal
        if (col-c) == -(row-r): return False # Check right diagonal
    return True

def solve(n):
    if n == 0: return [[]]
    smaller_solutions = solve(n-1)
    solutions = []
    for solution in smaller_solutions:
        for column in range(1,BOARD_SIZE+1):
            if safe(column , solution):
                solutions.append(solution + [(n,column)])
    return solutions

for answer in solve(BOARD_SIZE): print answer
