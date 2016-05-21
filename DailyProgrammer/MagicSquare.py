# A 3x3 magic square is a 3x3 grid of the numbers 1-9 such that each row, column,
# and major diagonal adds up to 15. Here's an example:
#
# 8 1 6
# 3 5 7
# 4 9 2
#
# Optional bonus 1
#
# Verify magic squares of any size, not just 3x3.

import math

def magicSquare(list):
    n = int(math.sqrt(len(list)))
    i = 0
    sum = 0

    # check horizontal
    while i < len(list):
        sum += list[i]
        if int(i+1) % int(n) == 0:
            if sum != 15:
                return 'false'
            else:
                sum = 0
        i+=1

    # check vertical
    for i in range(0,n):
        for j in range(0,n):
            sum += list[i + j*3]
            if j == n-1:
                if sum != 15:
                    return 'false'
                else:
                    sum = 0

    # check diagonal left -> right
    for i in range(0,n):
        sum += list[i*(n+1)]

    if sum != 15:
        return 'false'
    else:
        sum = 0

    # check diagonal right -> left
    for i in range(1,n+1):
        sum += list[i*(n-1)]

    if sum != 15:
        return 'false'
    else:
        sum = 0

    return 'true'


print magicSquare([8, 1, 6, 3, 5, 7, 4, 9, 2])
