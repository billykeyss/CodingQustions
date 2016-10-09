# https://www.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

def convert(a,b):
    add = a % b
    if a <= 1:
        return str(a)
    else:
        return str(convert(a//b,b)) + str(add)

for i in range(2,16):
    print "Base " + str(i) + ": " + str(convert(16,i))
