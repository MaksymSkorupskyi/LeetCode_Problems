"""121. Best Time to Buy and Sell Stock [Easy]

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

from typing import List


# Runtime: 1132 ms, faster than 29.40% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 52.04% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_price = None
        max_profit = 0
        for price in prices:
            if min_price is None or price < min_price:
                min_price = max_price = price
            max_price = max(max_price, price)
            max_profit = max(max_profit, max_price - min_price)

        return max_profit


# O(n) solution, works even for empty list
# Runtime: 856 ms, faster than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 80.56% of Python3 online submissions for Best Time to Buy and Sell Stock.
# https://leetcode.com/submissions/detail/508825288/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_price = None
        max_profit = 0
        for price in prices:
            if min_price is None or price < min_price:
                min_price = max_price = price
            elif price > max_price:
                max_price = price
                max_profit = max(max_profit, max_price - min_price)

        return max_profit


# Runtime: 916 ms, faster than 97.80% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.3 MB, less than 11.03% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10000  # Higher than upper constraint

        for price in prices:
            if price < min_price:
                min_price = price
            elif max_profit < price - min_price:
                max_profit = price - min_price

        return max_profit


def main():
    solution = Solution()
    for test_case, expected in (
            ([7, 1, 5, 3, 6, 4], 5,),
            ([7, 6, 4, 3, 1], 0),
            ([2, 4, 1], 2),
            ([2, 1, 2, 1, 0, 1, 2], 2),
            ([3, 2, 6, 5, 0, 3], 4),
            ([], 0),
            ([1], 0),

    ):
        print(test_case, solution.maxProfit(test_case), expected)
        assert solution.maxProfit(test_case) == expected


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
