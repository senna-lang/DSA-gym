# O(n)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1887854294
class MySolution:
    def maxProfit(self, prices: list[int]) -> int:
        maxPrice = 0
        profit = 0

        for p in reversed(prices):
            # Relax maxPrice from the future to the current position
            maxPrice = max(maxPrice, p)
            # Relax maxProfit using the current price
            # Guaranteed: p's index <= maxPrice's index
            profit = max(profit, maxPrice - p)

        return profit


class AdvanceSolution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0
        # Loop through each price starting from the second price (prices[1:])
        for p in prices[1:]:
            # If the current price (p) is less than the previously set buy_price, update buy_price to the current price.
            # This ensures that we buy at the lowest price possible.
            if buy_price > p:
                buy_price = p
            # Update profit to the maximum value between the current profit and the calculated profit.
            # This ensures we keep track of the maximum profit throughout the iteration.
            profit = max(profit, p - buy_price)

        return profit
