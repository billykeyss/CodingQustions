# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

# Options:
# Brute force
# Sort and search
# Keep dictionary of integers / boolean
# COOLEST SOLUTION: XOR cancels out duplicate numbers the final return value is the unique integer

def findUnique(inputList):
    uniqueinteger = 0
    for number in list:
        uniqueinteger = uniqueinteger ^ number
    return uniqueinteger
