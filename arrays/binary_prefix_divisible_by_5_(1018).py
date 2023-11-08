"""1018. Binary Prefix Divisible By 5 [Easy]

You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]

Example 3:

Input: nums = [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]

Example 4:

Input: nums = [1,1,1,0,1]
Output: [false,false,false,false,false]

Constraints:

1 <= nums.length <= 105
nums[i] is 0 or 1.
"""
from typing import List


# Runtime: 964 ms, faster than 13.09% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 15.2 MB, less than 52.76% of Python3 online submissions for Binary Prefix Divisible By 5.
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = ""
        r = []
        for n in nums:
            s += str(n)
            r.append(not (bool(int(s, base=2) % 5)))

        return r


# Runtime: 316 ms, faster than 56.03% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 15.2 MB, less than 52.76% of Python3 online submissions for Binary Prefix Divisible By 5.
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prefix = 0
        result = []
        for bit in nums:
            prefix = 2 * prefix + bit
            result.append(prefix % 5 == 0)

        return result


# Runtime: 108 ms, faster than 96.73% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 15.2 MB, less than 52.76% of Python3 online submissions for Binary Prefix Divisible By 5.
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prefix = 0
        result = []
        for bit in nums:
            prefix = 2 * prefix % 10 + bit
            result.append(prefix % 5 == 0)

        print(prefix)

        return result


def main():
    solution = Solution()
    print(solution.prefixesDivBy5([0, 1, 1]))
    print(solution.prefixesDivBy5([1, 1, 1]))
    print(solution.prefixesDivBy5([0, 1, 1, 1, 1, 1]))
    print(solution.prefixesDivBy5([1, 1, 1, 0, 1]))

    assert solution.prefixesDivBy5([0, 1, 1]) == [True, False, False]
    assert solution.prefixesDivBy5([1, 1, 1]) == [False, False, False]
    assert solution.prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False]
    assert solution.prefixesDivBy5([1, 1, 1, 0, 1]) == [False, False, False, False, False]


import time

timer = time.perf_counter()
main()
print(round((time.perf_counter() - timer) * 1000, 2), "ms")
