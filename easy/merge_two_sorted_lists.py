"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return Null pointer if result is an empty list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # list pointers
        merged_start = ListNode()
        merged = merged_start

        # null case
        if l1 == None and l2 == None:
            return None

        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 1000
            y = l2.val if l2 != None else 1000

            if x <= y:
                merged.val = x
                l1 = l1.next
            elif x > y:
                merged.val = y
                l2 = l2.next

            if l1 != None or l2 != None:
                new_node = ListNode()
                merged.next = new_node
                merged = new_node

        return merged_start
