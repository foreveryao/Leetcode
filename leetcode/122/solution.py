class Solution(object):
        def maxProfit(self, prices):
            total=0
            if prices[j+1]>prices[j]:
                total+=prices[j+1]-prices[j]
            return total
