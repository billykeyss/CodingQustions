# Check if a String is composed of all unique characters

def uniqueChars(string):
	return(len(set(string)) == len(string));

print uniqueChars('test')
print uniqueChars('qwertyuiop')
