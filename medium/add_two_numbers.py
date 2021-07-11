"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # loop pointers
        current_node = ListNode()
        sol_start = current_node
        l1_node = l1
        l2_node = l2
        carry = 0

        # loop to end of both lists
        while l1_node != None or l2_node != None:
            next_node = ListNode()
            x = l1_node.val if l1_node is not None else 0
            y = l2_node.val if l2_node is not None else 0

            total = x + y + carry

            if total < 10:
                current_node.val = total
                carry = 0
            else:
                current_node.val = total % 10
                carry = 1

            # advace list pointers
            l1_node = l1_node.next if l1_node != None else None
            l2_node = l2_node.next if l2_node != None else None

            # only add new node if not at end of list
            if l1_node != None or l2_node != None:
                current_node.next = next_node
                current_node = next_node

        if carry == 1:
            current_node.next = ListNode(val=1)

        return sol_start
