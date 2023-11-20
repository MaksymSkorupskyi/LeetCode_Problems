"""128. Longest Consecutive Sequence
Medium
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    @staticmethod
    def longest_consecutive_v1(nums: list[int]) -> int:
        """O(nlogn) sort"""
        if len(nums) < 2:
            return len(nums)

        # Sort the array
        nums.sort()
        max_consecutive = 0
        curr_consecutive = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                curr_consecutive += 1
            elif nums[i] - nums[i - 1] > 1:
                curr_consecutive = 1
            max_consecutive = max(max_consecutive, curr_consecutive)

        return max_consecutive
    @staticmethod
    def longest_consecutive_v2(nums: list[int]) -> int:
        """O(n) Set() cheat
        https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak/?envType=study-plan-v2&envId=top-interview-150
        First turn the input into a set of numbers.
        That takes O(n) and then we can ask in O(1) whether we have a certain number.

        Then go through the numbers.
        If the number x is the start of a streak (i.e., x-1 is not in the set),
        then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set.
        The length of the streak is then simply y-x
        and we update our global best with that.
        Since we check each streak only once, this is overall O(n).
        This ran in 44 ms on the OJ, one of the fastest Python submissions.
        """
        if len(nums) < 2:
            return len(nums)

        # O(n)
        nums = set(nums)
        longest_consecutive = 1
        # O(2n)
        for num in nums:
            if num - 1 not in nums:
                # has no left neighbor - start the sequence
                n = num + 1
                # O(3n)
                while n in nums:
                    n += 1
                longest_consecutive = max(longest_consecutive, n - num)

        return longest_consecutive


    @staticmethod
    def longest_consecutive_v3(nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # Create a hashmap of numbers and their count
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1

                if num - 1 in nums_map and num + 1 in nums_map:
                    # both neighbours - overlap two ranges
                    left = nums_map[num - 1]
                    right = nums_map[num + 1]
                    total = nums_map[num - left] + nums_map[num + right] + 1
                    nums_map[num - left] = total
                    nums_map[num + right] = total
                    # nums_map[num] = total

                elif num - 1 in nums_map:
                    # left neighbor
                    left = nums_map[num - 1]
                    nums_map[num - left] += 1
                    nums_map[num] = nums_map[num - left]

                elif num + 1 in nums_map:
                    # right neighbor
                    right = nums_map[num + 1]
                    nums_map[num + right] += 1
                    nums_map[num] = nums_map[num + right]

        return max(nums_map.values())

    @staticmethod
    def longest_consecutive_v4(nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # Create a hashmap of numbers and their count
        nums_map = {}
        longest_consecutive = 1
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1

                if num - 1 in nums_map and num + 1 in nums_map:
                    # both neighbours - overlap two ranges
                    left = nums_map[num - 1]
                    right = nums_map[num + 1]
                    total = nums_map[num - left] + nums_map[num + right] + 1
                    nums_map[num - left] = total
                    nums_map[num + right] = total
                    longest_consecutive = max(longest_consecutive, total)

                elif num - 1 in nums_map:
                    # left neighbor
                    left = nums_map[num - 1]
                    nums_map[num - left] += 1
                    nums_map[num] = nums_map[num - left]
                    longest_consecutive = max(longest_consecutive, nums_map[num])

                elif num + 1 in nums_map:
                    # right neighbor
                    right = nums_map[num + 1]
                    nums_map[num + right] += 1
                    nums_map[num] = nums_map[num + right]
                    longest_consecutive = max(longest_consecutive, nums_map[num])

        return longest_consecutive

    @staticmethod
    def longestConsecutive(nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        nums_map = {}
        longest_consecutive = 0
        for num in nums:
            if num not in nums_map:
                nums_map[num] = [num, num]
                left = num
                right = num

                # left neighbor - extend left range
                if num - 1 in nums_map:
                    left = nums_map[num - 1][0]

                # right neighbor - extend right range
                if num + 1 in nums_map:
                    right = nums_map[num + 1][1]

                nums_map[left] = [left, right]
                nums_map[right] = [left, right]
                longest_consecutive = max(longest_consecutive, right - left + 1)

        return longest_consecutive


test_cases = (
    ([1, 2, 0, 1], 3),
    ([], 0),
    ([0], 1),
    ([1, 2], 2),
    ([1, 2, 0], 3),
    ([1, 2, 3], 3),
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
)


for nums, expected in test_cases:
    result = Solution.longestConsecutive(nums)
    print(result)
    assert result == expected
