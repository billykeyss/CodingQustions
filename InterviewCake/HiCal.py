# Your company built an in-house calendar tool called HiCal. You want to add a
# feature to see the times in a day when everyone is available.

def availableChecker(list):
    list = sorted(list)
    cur_min = list[0][0]
    cur_max = list[0][1]
    avail = []

    i = 1
    while i < len(list):
        if list[i][0] > cur_max:
            cur_max=list[i-1][1]
            avail.append((cur_min, cur_max))
            cur_min = list[i][0]
            cur_max = list[i][1]
        else:
            cur_max = list[i][1]
        i+=1
    avail.append((cur_min, cur_max))
    print avail

availableChecker([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]);
availableChecker([(1, 3), (2, 4)]);
