"""714. Best Time to Buy and Sell Stock with Transaction Fee
Medium
You are given an array prices where prices[i] is the price of a given stock on the ith day,
and an integer fee representing a transaction fee.

Find the maximum profit you can achieve.
You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.

Note:
You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
1 <= prices.length <= 5 * 10^4
1 <= prices[i] < 5 * 10^4
0 <= fee < 5 * 10^4
"""


class Solution:
    @staticmethod
    def max_profit_time_limit_exceeded(prices: list[int], fee: int) -> int:
        # Initialize buying and selling prices tables
        # High buying price and 0 selling price initially
        buying_prices = [10 ** 5] * len(prices)
        selling_prices = [0] * len(prices)

        # Iterate over all stock prices
        for price in prices:
            # Iterate over each transaction
            buying_prices[0] = min(buying_prices[0], price)
            selling_prices[0] = max(selling_prices[0], price - buying_prices[0] - fee)
            for i in range(1, len(prices)):
                # Update min buying price
                buying_prices[i] = min(buying_prices[i], price - selling_prices[i - 1])
                # Update max selling price
                selling_prices[i] = max(selling_prices[i], price - buying_prices[i] - fee)

        # Maximum profit will be the last sell price
        return selling_prices[-1]

    @staticmethod
    def max_profit_v1(prices: list[int], fee: int) -> int:
        """pay the fee when buying the stock"""
        buy = 0  # Max profit from buying today
        sold = float("-inf")  # Max profit from selling today

        # Iterate through the stock prices
        for price in prices:
            sold = max(sold, buy - price - fee)
            buy = max(buy, sold + price)

        return buy

    @staticmethod
    def maxProfit(prices: list[int], fee: int) -> int:
        """pay the fee when buying the stock"""
        buy = 0  # Max profit from buying today
        sold = float("-inf")  # Max profit from selling today

        # Iterate through the stock prices
        for price in prices:
            sold = max(sold, buy - price)
            buy = max(buy, sold + price - fee)

        return buy


# Test cases
test_cases = (
    ([1, 3, 7, 5, 10, 3], 3, 6),
    ([1, 3, 2, 8, 4, 9], 2, 8),
)

# Validate against test cases
for prices, fee, expected in test_cases:
    result = Solution.maxProfit(prices, fee)
    print(result)
    assert result == expected
