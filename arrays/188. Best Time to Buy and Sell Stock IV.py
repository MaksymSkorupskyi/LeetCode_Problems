"""188. Best Time to Buy and Sell Stock IV
Hard
You are given an integer array prices where prices[i] is the price of a given stock on the ith day,
and an integer k.
Find the maximum profit you can achieve.
You may complete at most k transactions:
i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation:
Buy on day 2 (price = 2)
and sell on day 3 (price = 6), profit = 6-2 = 4.
Then buy on day 5 (price = 0)
and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""


class Solution:
    """The given code is a solution to the problem of finding the maximum profit
    that can be achieved by buying and selling a stock, given a maximum number of transactions k.
    The code uses dynamic programming to solve the problem.
    """

    @staticmethod
    def maxProfit(k: int, prices: list[int]) -> int:
        """
        1. The code defines a class called "Solution" with a static method "maxProfit"
        that takes two parameters:
            k (maximumnumber of transactions) and
            prices (an array of stock prices).

        2. The first condition checks if the length of the prices array is less than or equal to 1.
        If so, it means there are no prices or only one price,
        so the maximum profit that can be achieved is 0.

        3. The next condition checks if k is greater than the number of days in the prices array divided by 2.
        If so, it means we can perform unlimited transactions.
        In this case, the code calculates the profit by iterating over the prices array
        and adding the difference between consecutive prices whenever the price increases.
        This is done using a for loop and an if condition.
        The calculated profit is returned as the result.

        4. If the above conditions are not met, it means we have a limited number of transactions.
        The code initializes two lists: buying_price and selling_price.
        The buying_price list is initialized with a large value (10^5) for each transaction,
        and the selling_price list is initialized with 0 for each transaction.

        5. The code then iterates over each price in the prices array using a for loop.

        6. Inside the loop, another for loop is used to iterate over each transaction O(nk).
        This loop updates the buying_price and selling_price for each transaction.

        7. For each transaction, the code updates the buying_price
        by taking the minimum value between the current buying_price and the difference between
        the current price and the previous selling_price.
        This ensures that the buying_price is updated to the lowest possible value for the transaction.

        8. Similarly, the code updates the selling_price by taking the maximum value
        between the current selling_price and the difference between the current price
        and the current buying_price.
        This ensures that the selling_price is updated to the highest possible value for the transaction.

        9. After the inner loop completes,
        the code returns the last element of the selling_price list,
        which represents the maximum profit that can be achieved.

        In summary, the code uses dynamic programming to find the maximum profit
        that can be achieved by buying and selling a stock, given a maximum number of transactions.
        It handles both unlimited and limited transactions using different approaches.
        """
        # Base case - no profit if less than 2 prices
        if len(prices) <= 1:
            return 0

        # Special case - unlimited transactions If k is greater than a half number of days
        if k > len(prices) / 2:
            # Calculate profit by adding deltas of increasing prices
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        # Initialize buying and selling prices tables
        # High buying price and 0 selling price initially
        buying_prices = [10 ** 5 for _ in range(k)]
        selling_prices = [0 for _ in range(k)]

        # Iterate over all stock prices
        for price in prices:
            # Iterate over each transaction
            for i in range(k):
                # Update min buying price
                buying_prices[i] = min(
                    buying_prices[i],
                    price if i == 0 else price - selling_prices[i - 1],
                )
                # Update max selling price
                selling_prices[i] = max(
                    selling_prices[i],
                    price - buying_prices[i],
                )

        # Maximum profit will be the last sell price
        return selling_prices[-1]


# Test cases
test_cases = (
    (2, [3, 3, 5, 0, 0, 3, 1, 4], 6),
    (2, [1, 2, 4], 3),
    (1, [1, 2], 1),
    (4, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 15),
    (2, [2, 4, 1], 2),
    (2, [3, 2, 6, 5, 0, 3], 7),
    (1, [0, 1, 2, 3], 3),
)

# Validate against test cases
for k, nums, expected in test_cases:
    result = Solution.maxProfit(k, nums)
    print(result)
    assert result == expected
