# Find the shortest distance between two repeating numbers in an array

def shortestDist(list):
    i = 0
    shortestDistance = 0
    shortestDistDict = {}
    while i < len(list):
        for key in shortestDistDict:
            shortestDistDict[key] +=1
        if list[i] not in shortestDistDict:
            shortestDistDict[list[i]] = 0
        else:
            if shortestDistance > shortestDistDict[list[i]] or shortestDistance == 0:
                shortestDistance = shortestDistDict[list[i]]
        i+=1
    return shortestDistance


print shortestDist([1,2,3,4,2,6,1,3,6])
