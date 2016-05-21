# List all the prime numbers up till input x

def primeNumbersRemoving(integer):
    primeList = range(2,integer)
    i = 0
    while i < len(primeList):
        j = i + 1
        while j < len(primeList):
            if primeList[j] % primeList[i] == 0:
                primeList.remove(primeList[j])
            j+=1
        i+=1
    print primeList

def primeNumbersAppending(integer):
    list = []
    for num in range(2,integer):
        if all(num % i != 0 for i in range(2,num)):
           list.append(num)
    print list

primeNumbersRemoving(100)
primeNumbersAppending(100)
