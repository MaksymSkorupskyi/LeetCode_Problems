"""234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Runtime: 80 ms beats 100.00% of Python3 submissions, O(n) time and O(1) space
# https://leetcode.com/submissions/detail/150415387/
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        a = []
        curr_node = head
        while curr_node:
            a.append(curr_node.val)
            curr_node = curr_node.next
        return a == a[::-1]