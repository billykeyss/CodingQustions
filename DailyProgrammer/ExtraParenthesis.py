def parenthesis(inputString):
    pairs = []
    outputString = inputString
    i = 0
    while i < len(inputString):
        if inputString[i] == '(':
            pairs.append([i, -1])
        elif inputString[i] == ')':
            k = -1
            while pairs[k][1] != -1:
                k -= 1
            pairs[k][1] = i
        i+=1
    filter_list = []
    i=0
    while i < len(pairs):
        if pairs[i][0] == pairs[i][1] - 1:
            filter_list.append(pairs[i][0])
            filter_list.append(pairs[i][1])
        if i < len(pairs) - 1:
            if pairs[i][0] == pairs[i+1][0] - 1 and pairs[i][1] == pairs[i+1][1] + 1:
                filter_list.append(pairs[i][0])
                filter_list.append(pairs[i][1])
        i+=1
    filter_list = sorted(filter_list, reverse=True)
    for i in filter_list:
        outputString = outputString[:i] + outputString[i+1:]
    return outputString

    
print parenthesis('((a((bc)(de)))f)')
print parenthesis('ab((c))')
print parenthesis('(((zbcd)(((e)fg))))')
print parenthesis('()')
print parenthesis('((fgh()()()))')
print parenthesis('()(abc())')
