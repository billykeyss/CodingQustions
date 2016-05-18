# Problem 5
#
# Write a program that outputs all possibilities to put + or - or nothing
# between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100


ls = [2,3,4,5,6,7,8,9]

def calc(equation,list):
    equationCalc = ''.join(str(x) for x in equation)

    if len(list) == 0:
        if eval(equationCalc) == 100:
            print equationCalc
    else:
        calc(equation + ['+'] + list[0:1], list[1:])
        calc(equation + ['-'] + list[0:1], list[1:])
        calc(equation + list[0:1], list[1:])

calc([1],ls)
