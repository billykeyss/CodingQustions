days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth", "eleventh", "twelfth"]
gifts = ["a Patridge in a Pear Tree", "Two Turtle Doves", "Three French Hens", "Four Calling Birds", "Five Golden Rings", "Six Geese a Laying", "Seven Swans a Swimming", "Eight Maids a Milking", "Nine Ladies Dancing", "Ten Lords a Leaping", "Eleven Pipers Piping", "Twelve Drummers Drumming"]
i = 0
for day in days:
    print("On the " + day + " day of Christmas\nMy true love gave gave to me:")
    j = i
    while j >= 0:
        if i > 0 and j == 0:
            print("and " + gifts[j])
        else:
            print(gifts[j])
        j -= 1
    print("")
    i += 1
