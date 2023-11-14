"""202. Happy Number
Easy
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 231 - 1
"""


class Solution:
    @staticmethod
    def is_happy_v1(num: int) -> bool:
        """v1: hash map"""
        num_map = {}
        size = 0
        while num != 1:
            num = num_map.setdefault(num, sum([int(n) ** 2 for n in str(num)]))
            if size == len(num_map) and num != 1:
                # Endless loop
                return False

            size = len(num_map)

        return True

    @staticmethod
    def isHappy(num: int) -> bool:
        """v2: hash set"""
        num_set = set()
        while num != 1:
            if num in num_set:
                return False

            num_set.add(num)
            num = sum([int(n) ** 2 for n in str(num)])

        return True


test_cases = (
    (19, True),
    (2, False),
)
for n, answer in test_cases:
    result = Solution.isHappy(n)
    print(result)
    assert result == answer
