# Change the a sentence to another sentence, letter by letter.
# The sentences will always have the same length.
def changeSentence(input1, input2):
    if input1 == input2:
        print input1
        return
    input1Array = list(input1)
    input2Array = list(input2)
    i = 0
    for i in range(len(input1Array)):
        if input1Array[i] != input2Array[i]:
            input1Array[i] = input2Array[i]
            print ('').join(input1Array)
        i+=1
    print
changeSentence('floor', 'brake')
changeSentence('wood', 'book')
changeSentence('a fall to the floor', 'braking the door in')
