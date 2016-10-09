# You'll be given two words or sets of words separated by a question mark. Your task is to replace the question mark with information about the validity of the anagram. Example:
# "Clint Eastwood" ? "Old West Action"
# "parliament" ? "partial man"
#
# "Clint Eastwood" is an anagram of "Old West Action"
# "parliament" is NOT an anagram of "partial man"
# https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/


def anagramDet(anagramString):
    firstString = anagramString.split("?")[0].lower()
    secondString = anagramString.split("?")[1].lower()

    firstStringSorted = ''.join(sorted(firstString.replace(" ", "").replace('"', "")))
    secondStringSorted = ''.join(sorted(secondString.replace(" ", "").replace('"', "")))

    if firstStringSorted != secondStringSorted:
        return firstString + " is NOT an anagram of " + secondString
    else:
        return firstString + " is an anagram of " + secondString


print anagramDet('"Clint Eastwood" ? "Old West Action"')
print anagramDet('"parliament" ? "partial man"')
print anagramDet('"wisdom" ? "mid sow"')
print anagramDet('"Seth Rogan" ? "Gathers No"')
print anagramDet('"Reddit" ? "Eat Dirt"')
print anagramDet('"Schoolmaster" ? "The classroom"')
print anagramDet('"Astronomers" ? "Moon starer"')
print anagramDet('"Dormitory" ? "Dirty Rooms"')
