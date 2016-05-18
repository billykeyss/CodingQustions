# Write fibbonaci iteratively and recursively (bonus: use dynamic programming)
# USe dynamic programming? Research this

def createFibIteratively(length):
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

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print fib(10)
createFibIteratively(100)
