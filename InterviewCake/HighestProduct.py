# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

def highestProduct(list):
    maxNumber1=list[0]
    maxNumber2=list[0]
    maxNumber3=list[0]
    minNumber1=list[0]
    minNumber2=list[0]

    for number in list:
        if number > maxNumber1:
            maxNumber3=maxNumber2
            maxNumber2 = maxNumber1
            maxNumber1 = number
        elif number > maxNumber2:
            maxNumber3=maxNumber2
            maxNumber2 = number
        elif number > maxNumber3:
            maxNumber3 = number
        elif number < minNumber1:
            minNumber2 = minNumber1
            minNumber1 = number
        elif number < minNumber2:
            minNumber2 = number

    if minNumber1 * minNumber2 > maxNumber1 * maxNumber2:
        print minNumber1 * minNumber2 * maxNumber1
    else:
        print maxNumber1*maxNumber2*maxNumber3

highestProduct([1, 10, -5, 1, -100])
highestProduct([-10, -10, 1, 3, 2])
