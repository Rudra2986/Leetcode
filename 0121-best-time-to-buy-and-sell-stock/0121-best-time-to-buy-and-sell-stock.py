class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        cheapest_so_far = max(prices)

        for i in range(len(prices)):
            profit = 0


            if prices[i] < cheapest_so_far:
                cheapest_so_far = prices[i]


            profit = prices[i] - cheapest_so_far

            if profit > max_profit :
                max_profit = profit

        return max_profit