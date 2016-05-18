# Problem 3
#
# Write a function that computes the list of the first 100 Fibonacci numbers.
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
# and each subsequent number is the sum of the previous two. As an example,
# here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def createFib(length):
    fibList = [0, 1]
    if length == 0:
        print fibList[0]
        return
    if length == 1:
        print fibList[0]
        return
    if length == 2:
        print fibList
        return

    i = 2
    while i < length:
        sum = fibList[i-1] + fibList[i-2]
        fibList.append(sum)
        i+=1
    print fibList

createFib(100)
