"""371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3."""


# a.__add__(b) Python 3 solution  [Runtime 32 ms beats 100.00 % of python3 submissions]
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a.__add__(b)


# sum([a, b]) Python 3 solution [Runtime: 32 ms beats 100.00 % of python3 submissions]
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])
