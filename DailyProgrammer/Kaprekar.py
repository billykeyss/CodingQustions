def kaprekarRoutine(number, iteration):
    if number == 6174:
        return iteration
    number = str(number).zfill(4)
    newNum = sortOrder(number, True) - sortOrder(number, False)
    if newNum == 6174:
        return iteration + 1
    else:
        return kaprekarRoutine(newNum, iteration + 1)
def largest_digit(number):
    numberList = [int(x) for x in str(number)]
    largestNumber = 0
    for num in numberList:
        if largestNumber < num:
            largestNumber = num
    return largestNumber
def sortOrder(number, ascending):
    number = str(number).zfill(4)
    numberList = [int(x) for x in str(number)]
    return int(''.join(sorted(number, reverse=ascending)))
print kaprekarRoutine(4567, 0)
print kaprekarRoutine(4167, 0)
print kaprekarRoutine(6589, 0)
print kaprekarRoutine(5455, 0)
print kaprekarRoutine(6174, 0)



def kaprekar(number):
    square = [int(x) for x in str(number * number)]
    if number == 1:
        return True
    for i in range(1, len(square)):
        if number == int(''.join(map(str, square[i:]))) + int(''.join(map(str, square[:i]))):
            return True
    return False
# print [i for i in range(1, 50) if kaprekar(i)]
# print [i for i in range(2, 100) if kaprekar(i)]
print [i for i in range(0, 9000) if kaprekar(i)]
