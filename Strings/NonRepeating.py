# Find the first word in a stream in which it is not repeated in the rest of the stream.
# Please note that you are being provided a stream as a source for the characters.
# The stream is guaranteed to eventually terminate (i.e. return false from a call to the hasNext() method), though it could be very long.
# You will access this stream through the provided interface methods. A call to hasNext() will return whether the stream contains any more characters to process. A call to getNext() will return the next character to be processed in the stream. It is not possible to restart the stream.

def wordlist(s):
	wordlist=[]
	s = s.lower()
	for i in s.replace('.','').split():
		if i in wordlist:
			wordlist.remove(i)
		else:
			wordlist.append(i)

	return wordlist
