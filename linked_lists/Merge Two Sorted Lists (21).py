"""21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# v1: Runtime 44 ms beats 99.95 % of python3 submissions.
class Solution:
    def mergeTwoLists(self, l1, l2):
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
        l3 = head = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return head.next


# v2 stack solution: Runtime 48 ms beats 97.38 % of python3 submissions.
class Solution:
    def mergeTwoLists(self, l1, l2):
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
        stack = []
        while l1:
            stack.append(l1.val)
            l1 = l1.next
        while l2:
            stack.append(l2.val)
            l2 = l2.next
        stack.sort()
        l3 = head = ListNode(stack[0])
        for i in range(1, len(stack)):
            head.next = ListNode(stack[i])
            head = head.next
        return l3
