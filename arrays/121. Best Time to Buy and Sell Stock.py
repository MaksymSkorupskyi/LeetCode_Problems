"""121. Best Time to Buy and Sell Stock
Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed
because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""


class Solution:
    @staticmethod
    def max_profit_v1(prices: list[int]) -> int:
        min_price = 1
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)

        return max_profit

    @staticmethod
    def max_profit_v2(prices: list[int]) -> int:
        max_profit = 0
        left = 0  # buy
        right = 1  # sell
        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit

    @staticmethod
    def maxProfit(prices: list[int]) -> int:
        buying_price = 10 ** 5
        selling_price = 0

        for price in prices:
            # Update the minimum buying price for the transaction
            buying_price = min(buying_price, price)

            # Update the maximum selling price for the transaction
            selling_price = max(selling_price, price - buying_price)

        return selling_price


test_cases = (
    ([1, 2], 1),
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 4, 1], 2),
    ([2, 1, 2, 1, 0, 1, 2], 2),
    ([3, 2, 6, 5, 0, 3], 4),
    ([], 0),
    ([1], 0),
)

for nums, expected in test_cases:
    result = Solution.maxProfit(nums)
    print(result)
    assert result == expected
