# Given an integer, write a function to determine if it is a power of two.

# 56ms runtime beats 100% of Python solutions (recursion)
# https://leetcode.com/submissions/detail/142983889/
# https://discuss.leetcode.com/topic/120779/56ms-runtime-beats-100-of-python-solutions-recursion

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n in [1, 2]:
            return True
        else:
            if n % 2:
                return False
            else:
                return self.isPowerOfTwo(n / 2)

def main():
    a = Solution()
    for i in range(-1, 65):
        print(i, a.isPowerOfTwo(i))

main()