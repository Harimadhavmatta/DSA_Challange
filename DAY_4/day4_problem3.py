class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        for i in prices:
            profit=i-min_price
            max_profit=max(profit,max_profit)
            min_price=min(i,min_price)
        return max_profit
