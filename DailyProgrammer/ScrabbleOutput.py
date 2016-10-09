# Scrabble output
def testScrabble(inputString) :
    scrabbleDict = {'E': 12,
            'A': 9,
            'I': 9,
            'O': 8,
            'N': 6,
            'R': 6,
            'T': 6,
            'L': 4,
            'S': 4,
            'U': 4,
            'D': 4,
            'G': 3,
            '_': 2,
            'B': 2,
            'C': 2,
            'M': 2,
            'P': 2,
            'F': 2,
            'H': 2,
            'V': 2,
            'W': 2,
            'Y': 2,
            'K': 1,
            'J': 1,
            'X': 1,
            'Q': 1,
            'Z': 1}

    inputString = inputString.upper()

    for c in inputString:
        scrabbleDict[c] -= 1

    result = {}
    for k, v in scrabbleDict.items():
        result[v] = result.get(v, []) + [k]

    print result
    if -1 in result:
        print('Invalid input. More {} have been taken from the bag than possible.'.format('\'s, '.join(result[-1][:-1]) + '\'s and {}\'s'.format(result[-1][-1]) if len(result[-1]) > 1 else result[-1][0] + '\'s'))
    else:
        print(''.join(['{}: {}\n'.format(k, ', '.join(sorted(v))) for k, v in sorted(result.items(), reverse=True)]))

testScrabble('AEERTYOXMCNB_S')
testScrabble('AXHDRUIOR_XHJZUQEE')
