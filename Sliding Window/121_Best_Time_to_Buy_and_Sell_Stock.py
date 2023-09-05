class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n), where n is the length of prices
        Space: O(1)
        """
        max_profit = 0
        left, right = 0, 1

        # Buy low, sell high for max profit
        while left < right < len(prices):
            if prices[right] - prices[left] > max_profit:
                max_profit = max(prices[right] - prices[left], max_profit)
            elif prices[right] < prices[left]:
                left = right
            right += 1

        return max_profit
