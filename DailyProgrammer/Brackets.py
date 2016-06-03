# Return all valid combinations of parenthesis

def brackets(amount, left=0, right=0, output = ''):
    if left==amount and right == amount:
        print output
    else:
        if right < left:
            brackets(amount , left, right+1, output + ")")
        if left < amount:
            brackets(amount , left+1, right, output + "(")

brackets(3)
