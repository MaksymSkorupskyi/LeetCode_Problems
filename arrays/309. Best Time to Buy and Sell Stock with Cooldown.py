"""309. Best Time to Buy and Sell Stock with Cooldown
Medium
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""


class Solution:
    """The code is a solution to the "Best Time to Buy and Sell Stock with Cooldown" problem.
    Given an array of stock prices,
    the code finds the maximum profit that can be achieved with the following restrictions:
    1. after selling a stock, there must be a cooldown period of one day before buying another stock,
    2. and only one stock can be held at a time.
    """

    @staticmethod
    def maxProfit(prices: list[int]) -> int:
        """The code uses dynamic programming to keep track of the maximum profit
        that can be achieved at each day, considering the three possible actions:
            1) selling,
            2) holding, or
            3) resting (i.e., not buying or selling).

        Step by step explanation:

        1. Define three variables: sold, hold, and rest,
        initialized to 0, float('-inf'), and 0, respectively.
        These variables represent the maximum profit that can be achieved at the current day,
        considering the three possible actions: selling, holding, or resting.

        2. Loop through the prices array, and for each day, update the three variables as follows:
        - hold = max(hold, rest - price)
            (hold the stock bought before yesterday
            or buy the stock today if it results in a higher profit)
        - rest = max(rest, hold)
            (do not buy or sell today, keep the maximum profit achieved before today)
        - sold = hold + price
            (sell the stock held yesterday and buy the stock at the current price)

        3. Return the maximum profit achieved at the end of the loop,
        which is the maximum value of rest and sold.
        """
        # Max profit from selling today
        sold = 0

        # Max profit from holding stock from previous day
        hold = float("-inf")

        # Max profit from not buying/selling today
        rest = 0

        # Iterate through the stock prices
        for price in prices:
            # Hold either previous held stock, or buy new stock today
            # Buying new stock today costs "rest - price"
            hold = max(hold, rest - price)

            # Rest keeps previous max rest profit
            # Also keeps max sold profit from previous iteration
            rest = max(rest, sold)

            # Sell stock that was held yesterday
            # Add today's price to get sell profit
            sold = hold + price

        # Final max profit is max of sold or rest states
        return max(rest, sold)


# Test cases
test_cases = (
    ([2, 1], 0),
    ([1, 2, 3, 0, 2], 3),
    ([1], 0),
)
# Validate against test cases
for prices, expected in test_cases:
    result = Solution.maxProfit(prices)
    print(result)
    assert result == expected
