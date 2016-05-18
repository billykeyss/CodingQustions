# Given 2 integer arrays, determine of the 2nd array is a rotated version of the
# 1st array. Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}

def findRotated(list1,list2):
    firstList = list1 + list1
    list2 = ''.join(str(x) for x in list2)
    firstList = ''.join(str(x) for x in firstList)
    print list2 in firstList


findRotated([1,2,3,5,6,7,8],[5,6,7,8,1,2,3])
