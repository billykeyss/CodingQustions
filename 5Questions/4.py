# Problem 4
#
# Write a function that given a list of non negative integers, arranges them
# such that they form the largest possible number. For example, given
# [50, 2, 1, 9], the largest formed number is 95021.

def largestNumber(list):
    number = []
    optionone = []
    optiontwo = []
    i = 0
    while i < len(list):
        optionone.append(list[i])
        optiontwo = [list[i]] + optiontwo
        if ''.join(str(char) for char in optiontwo) < ''.join(str(char) for char in optionone):
            number.append(list[i])
        else:
            number = [list[i]] + number
        i+=1
    print ''.join(str(char) for char in number)


largestNumber([50,2,1,9]);
