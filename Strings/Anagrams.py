# Determine if 2 Strings are anagrams

def anagramSolver(string1, string2):
    string1 = ''.join(sorted(string1.replace(" ", "")))
    string2 = ''.join(sorted(string2.replace(" ", "")))
    if string1 == string2:
        print 'true'
    else:
        print 'false'

anagramSolver('anagram', 'nag a ram');
