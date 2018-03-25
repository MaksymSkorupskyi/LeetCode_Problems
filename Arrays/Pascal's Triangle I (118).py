"""118. Pascal's Triangle I
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5, Return:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]"""

# Binomial Coefficient 40 ms runtime beats 91.08% of Python 3 submissions.

class Solution:
    def factorial(self, n):
        if n in [0, 1]:
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

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascale_triangle = []
        for i in range(0, numRows):
            pascale_triangle.append(self.getRow(i))
        return pascale_triangle


def main():
    a = Solution()
    # print(a.generate(5))
    for k in range(10):
        print(k, a.generate(k))


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), 'ms')