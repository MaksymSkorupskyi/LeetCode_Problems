"""445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# int-to-str: Runtime 116ms beats 99.43 % of python3 submissions.
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # check that linked lists l1 and l2 are not empty
        if not l1:
            return l2
        if not l2:
            return l1
        # initializing x1, x2
        x1 = x2 = ''
        # extracting number x1 from linked list l1
        while l1:
            x1 += str(l1.val)
            l1 = l1.next
        # extracting number x2 from linked list l2
        while l2:
            x2 += str(l2.val)
            l2 = l2.next
        # Add Two Numbers: y = x1 + x2
        y = int(x1) + int(x2)
        y = str(y)
        # make result
        head = new_node = ListNode(y[0])
        for i in range(1, len(y)):
            new_node.next = ListNode(y[i])
            new_node = new_node.next
        return head