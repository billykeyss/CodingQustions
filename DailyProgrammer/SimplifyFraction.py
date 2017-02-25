# You will be given a list with 2 numbers seperator by a space. The first is the numerator, the second the denominator
# 4 8
# 1536 78360
# 51478 5536
# 46410 119340
# 7673 4729
# 4096 1024
# Output description
#
# The most simplified numbers
# 1 2
# 64 3265
# 25739 2768
# 7 18
# 7673 4729
# 4 1

def gcd(a,b):
    while a:
        b, a = a, b%a
    return b

def simplifyFraction(x,y):
    return x / gcd(x,y), y / gcd(x,y)

print simplifyFraction(4, 8)
print simplifyFraction(1536, 78360)
print simplifyFraction(51478, 5536)
print simplifyFraction(46410, 119340)
print simplifyFraction(7673, 4729)
print simplifyFraction(4096, 1024)
