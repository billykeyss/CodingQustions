# Find the most frequent integer in an array

def freqInteger(list):
    frequencyList = {}
    for number in list:
        if number in frequencyList:
            frequencyList[number] += 1
        else:
            frequencyList[number] = 1

    print max(frequencyList.iterkeys(), key=lambda k: frequencyList[k])

freqInteger([1,1,2,3,4,5,6,2,3,4,2,2,34,2]);
