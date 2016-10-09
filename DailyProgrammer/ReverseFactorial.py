# Given a number, reverse it to find out what kind of factorial it is, i.e. 120 -> 5!
# https://www.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/

def reverseFactorial(factorialNumber):
    i = 2
    factorialNumber = factorialNumber + 0.0;

    while factorialNumber > 1:
        factorialNumber = factorialNumber / i
        if factorialNumber == 1:
            return str(i) + "!"
        i+=1

    return "Not a Factorial"

print reverseFactorial(120)
print reverseFactorial(150)
print reverseFactorial(720)
print reverseFactorial(3628800)
print reverseFactorial(479001600)
print reverseFactorial(6)
print reverseFactorial(18)
