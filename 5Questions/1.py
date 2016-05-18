# Problem 1
#
# Write three functions that compute the sum of the numbers
#  in a given list using a for-loop, a while-loop, and recursion.

def forSum(list):
    sum = 0
    for number in list:
        sum = sum + number

    print sum

def whileSum(list):
    sum = 0
    i = 0
    while i < len(list):
        sum = sum + list[i]
        i+=1

    print sum

def recurseSum(list, sum):
    if(len(list) == 0):
        print sum
    else:
        sum += list.pop(0)
        recurseSum(list, sum)

forSum([1,2,3,4,5]);
whileSum([1,2,3,4,5]);
recurseSum([1,2,3,4,5], 0);
