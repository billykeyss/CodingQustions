# Find the only element in an array that only occurs once.

def findUnique(list):
    frequencyList = {}
    for number in list:
        if number in frequencyList:
            frequencyList[number] += 1
        else:
            frequencyList[number] = 1

    print min(frequencyList.iterkeys(), key=lambda k: frequencyList[k])

findUnique([1,2,3,2,1,2,3,4,5,1,4])
