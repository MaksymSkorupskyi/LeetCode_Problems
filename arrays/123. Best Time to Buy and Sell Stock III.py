"""123. Best Time to Buy and Sell Stock III
Hard

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the
same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
"""


class Solution:
    @staticmethod
    def maxProfit(prices: list[int]) -> int:
        """You have two transactions,
        you are trying to minimize first buy with lowest out of pocket
        and maximize remaining amount after second purchase against profit1.
        The key to this problem is the sliding window concept in first buy.

        This code solves the problem of finding the maximum profit
        that can be achieved by buying and selling stocks.
        The function maxProfit takes a list of stock prices as input
        and returns the maximum profit that can be obtained by completing at most two transactions.
        The code uses a sliding window approach to minimize the buying price
        and maximize the selling price for each transaction.
        The final result is the maximum selling price after the second transaction.
        """
        buying_price_1 = 10 ** 5
        buying_price_2 = 10 ** 5
        selling_price_1 = 0
        selling_price_2 = 0

        for price in prices:
            # Update the minimum buying price for the first transaction
            buying_price_1 = min(buying_price_1, price)

            # Update the maximum selling price for the first transaction
            selling_price_1 = max(selling_price_1, price - buying_price_1)

            # Update the minimum buying price for the second transaction
            buying_price_2 = min(buying_price_2, price - selling_price_1)

            # Update the maximum selling price for the second transaction
            selling_price_2 = max(selling_price_2, price - buying_price_2)

        return selling_price_2


test_cases = (
    ([1, 500, 5, 1000], 1494),
    ([3, 3, 5, 0, 0, 3, 1, 4], 6),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2], 1),
    ([2, 4, 1], 2),
    ([], 0),
    ([1], 0),
)

for nums, expected in test_cases:
    result = Solution.maxProfit(nums)
    print(result)
    assert result == expected
