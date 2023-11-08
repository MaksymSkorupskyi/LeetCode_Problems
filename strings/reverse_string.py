"""344. Reverse a string

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

from typing import List


# Runtime: 152 ms, faster than 99.53% of Python3 online submissions for Reverse String.
# Memory Usage: 17.5 MB, less than 77.84% of Python3 online submissions for Reverse String.
class Solution:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s


def main():
    solution = Solution()
    for s in (
            ["h", "e", "l", "l", "o"],
            ["H", "a", "n", "n", "a", "h"]
    ):
        print(solution.reverseString(s))


if __name__ == "__main__":
    import time

    timer = time.perf_counter()
    main()
    print(round((time.perf_counter() - timer) * 1000, 2), "ms")
