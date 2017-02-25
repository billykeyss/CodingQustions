# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.
#
# Each type of cake has a weight and a value, stored in a tuple with two indices:
#
# An integer representing the weight of the cake in kilograms
# An integer representing the monetary value of the cake in British pounds
# For example:
#
#   # weighs 7 kilograms and has a value of 160 pounds
# (7, 160)
#
# # weighs 3 kilograms and has a value of 90 pounds
# (3, 90)
#
# You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.
#
# Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.
#
# For example:
#
#   cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20
#
# max_duffel_bag_value(cake_tuples, capacity)
# # returns 555 (6 of the middle type of cake and 1 of the last type of cake)
#

def max_duffel_bag_value(cake_array, capacity):
    # Add one cake to the bag at a time, based on capacity allowances and highest price to kg ratio
    # Calculate price per kilo, fill in the rest
    if capacity == 0:
        return 0

    while (0,0) in cake_array:
        cake_array.pop(cake_array.index((0,0)))


    # First iteration
    maxPriceRatio, maxPriceRatioCake = maxPriceRatioFunc(cake_array, capacity)

    amountCake = capacity / maxPriceRatioCake[0]
    amountCapacity = capacity - maxPriceRatioCake[0] * amountCake
    totalValue = amountCake * maxPriceRatioCake[1]

    # Second Iteration
    cake_array.pop(cake_array.index(maxPriceRatioCake));

    maxPriceRatio, maxPriceRatioCake = maxPriceRatioFunc(cake_array, amountCapacity)

    amountCake = amountCapacity / maxPriceRatioCake[0]
    amountCapacity = amountCapacity - maxPriceRatioCake[0] * amountCake
    totalValue += amountCake * maxPriceRatioCake[1]

    return totalValue

def maxPriceRatioFunc(cake_array, capacity):
    maxPriceRatio = 0
    for cake in cake_array:
        if cake[0] > capacity:
            continue
        cakePriceRatio = float(cake[1]) / float(cake[0])
        if maxPriceRatio < cakePriceRatio:
            maxPriceRatio = cakePriceRatio
            maxPriceRatioCake = cake

    return maxPriceRatio, maxPriceRatioCake



ct= [(7,160), (3,90), (2,15), (50,15), (10,1), (1, 5), (6, 140)]
cap = 20

print max_duffel_bag_value(ct, cap)
