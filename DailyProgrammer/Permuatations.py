#https://www.reddit.com/r/dailyprogrammer/comments/4i3xrm/20160504_challenge_265_hard_permutations_with/

def permutations(list):
    print factorial(len(list))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

permutations([8,8,8,8,8 ,8, 8, 8, 8, 7, 7, 7, 6, 5, 0, 1, 2, 5, 0, 1, 2, 0, 0, 1, 1, 5, 4, 3, 2, 1, 0,6,7,8])
