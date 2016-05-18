# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)

def findPairs(list):
    i = 0
    while i < len(list):
        if list[i] < 10:
            for secondNumber in list[i+1:]:
                if list[i] + secondNumber == 10:
                    print str(list[i]) + ', ' + str(secondNumber)
        i+=1

findPairs([1,5,2,3,4,5,2,4,7,6,5,4,3]);
