# Your dog just won X place in a dog show, congratulations! You post your star's
# photo and placement announcement to /r/aww and, predictably, a funny redditor
# asks what places the rest of the participating dogs took. Your job is to create
#  a program that lists all places within the range of 0-100 in spoken English,
#  excluding the placing (X) of your winning pup.

# Input description
# Input is the integer placement of your dog (X) within the range 0-100.

# Output description
# A reader should see a neatly formatted list of placements from 0-100 in spoken
# English, excluding your dog's placement.

def dogPlace(position):
    for i in range(100):
        if i == position:
            continue
        elif i % 10 == 1 and i % 100 != 11:
            print(str(i)+'st'+','),
        elif i % 10 == 2 and i %100 != 12:
            print(str(i)+'nd'+','),
        elif i % 10 == 3 and i %100 != 13:
            print(str(i)+'rd'+','),
        else:
            print(str(i)+'th'+','),

dogPlace(5)
