# Check if String is a palindrome

def palindrome(string):
    testString = string[::-1]
    if string == testString:
        return 'true'
    else:
        return 'false'

print palindrome('racecar')
