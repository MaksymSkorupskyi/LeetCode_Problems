"""92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list."""

# Runtime: 36 ms beats 99.63 % of python3 submissions.
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head.next or m == n: # no sense for reverse
            return head
        prev_node = None
        curr_node = head
        for i in range(1, m): # iterating over linked list to find M-node
            prev_node = curr_node
            curr_node = curr_node.next
        before_m_node = prev_node # remember node before M-node
        m_node = curr_node # remember M-node
        next_node = curr_node.next  # Remember next node
        for i in range(m, n):
            prev_node = curr_node
            curr_node = next_node  # Move to next node.
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE!
        m_node.next = next_node # redirecting M-node to ex-N+1 node
        if before_m_node:
            before_m_node.next = curr_node # redirecting M-1 node to N-node
        else:
            head = curr_node
        return head