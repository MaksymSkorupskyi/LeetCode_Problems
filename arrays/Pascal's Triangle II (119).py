"""119. Pascal's Triangle II
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
# Binomial Coefficient 40 ms runtime beats 91.77 % of Python 3 submissions.


class Solution:
    def factorial(self, n):
        if n < 2:
            return 1
        return n * Solution.factorial(self, n - 1)

    def getRow(self, n):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = []
        for k in range(n + 1):
            row.append(self.factorial(n) // (self.factorial(k) * self.factorial(n - k)))
        return row


# v2: faster lambda solution


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            res = list(map(lambda x, y: x + y, [0] + res, res + [0]))
            # print(i, res)
        return res


def main():
    a = Solution()
    # print(a.getRow(3))
    for k in range(100):
        print(k, a.getRow(k))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
