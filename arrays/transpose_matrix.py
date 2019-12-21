"""867. Transpose Matrix
Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Runtime: 72 ms, faster than 91.68% of Python3 online submissions for Transpose Matrix.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Transpose Matrix.
"""

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
