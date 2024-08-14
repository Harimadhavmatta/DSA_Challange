# Best Time to Buy and Sell Stocks II (Medium)
# This solution uses a greedy approach by capturing every increase in stock price.
# It accumulates the profit whenever the price on the next day is higher than the current day.
class Solution:
    def maxProfit(self, prices):
        profit = 0  
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit
