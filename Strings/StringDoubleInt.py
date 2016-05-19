# Determine if a String is an int or a double

def intDouble(string):
    for char in string:
        if char == ".":
            return 'true'

    return 'false'

print intDouble("1.5")
print intDouble("2")
