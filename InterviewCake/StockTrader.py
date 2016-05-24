# Suppose we could access yesterday's stock prices as a list, where:
#
# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

def maxProfit(stockList):
    min_price = stockList[0]
    max_profit = 0

    for price in stockList:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price-min_price

    return max_profit


print maxProfit([10, 7, 5, 8, 11, 9])
