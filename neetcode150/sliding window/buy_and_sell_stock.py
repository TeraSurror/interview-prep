class Solution:
    def max_profit(self, prices):
        result = 0
        lowest = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            result = max(result, prices[i] - lowest)

        return result
