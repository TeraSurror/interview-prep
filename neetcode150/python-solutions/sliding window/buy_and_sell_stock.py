from typing import List


def max_profit(prices: List[int]) -> int:
    max_profit: int = 0
    curr_min: int = prices[0]
    for num in prices:
        curr_min = min(num, curr_min)
        curr_profit = num - curr_min
        max_profit = max(curr_profit, max_profit)

    return max_profit
