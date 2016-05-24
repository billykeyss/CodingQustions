# You have a list of integers, and for each index you want to find the product of
# every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list
# of integers and returns a list of the products.

# Do not use division in your solution.

def produceProductList(list):
    productList = [1]
    i = 0
    while i < len(list) - 1:
        productList.append(list[i] * productList[i])
        i+=1

    print productList

    productListReverse = [1]
    j = 0
    i = len(list) - 1
    while i > 0:
        productListReverse.append(list[i] * productListReverse[j])
        j+=1
        i-=1
    productListReverse.reverse()

    finalProductList = []
    i = 0
    while i < len(list):
        finalProductList.append(productList[i] * productListReverse[i])
        i+=1

    print finalProductList

# [1, 1*7, 1*7*3, 1*7*3*4] -> [1d   , 1  ,1*7, 1*7*3] -> [1,1,7,21]
# [1*7*3*4, 7*3*4, 4*3, 4] -> [7*3*4, 3*4,4  , 1d    ] -> [84,12,4,1]  [1,4,12,84]
# Desired: [7*3*4, 1*3*4, 1*7*4, 1*7*3]


produceProductList([1, 7, 3, 4])
