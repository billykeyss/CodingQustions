# Problem 2
#
# Write a function that combines two lists by alternatingly taking elements.
# For example: given the two lists [a, b, c] and [1, 2, 3],
# the function should return [a, 1, b, 2, c, 3].

def combineList(list1,list2):
    i = 0
    combinedList=[]
    while i < len(list1):
        combinedList.append(list1[i])
        combinedList.append(list2[i])
        i+=1
    print combinedList

combineList(['a','b','c'] , [1,2,3])
