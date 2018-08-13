#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Input: 4->2->1->3
# 2->4->1->3    put 4 in the right place, now first 2 items are sorted
# 1->2->4->3    put 1 in the right place, now 3 items are sorted
# 1->2->3->4    put 3 in the right place, now all 4 items are sorted 
# Output: 1->2->3->4

class Solution(object):
    def insertionSortList(self, head):
        """Sorts a linked list using the insertion sort algorithm

        This algorithm should work in the following manner:
        1. Each iteration there is a current node which we need to put in the correct position. When we start, it is the first
        node. 
        2. We traverse the list until we find the correct position. This correct position is before a node with a value
        greater than the current node's. We can also reach the end of the list without finding any such node. In this case, 
        we insert at the end.
        3. Continue doing so, until current is None. 

        Because we are dealing with a linked list, we insert by relinking pointers. Having a dummy head should
        eliminate special cases.
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current:
            prev = dummy
            nxt = prev.next
            while nxt != current:
                if current.val < nxt.val:
                    tmp = nxt
                    while tmp.next != current:
                        tmp = tmp.next
                    rest = current.next
                    prev.next = current
                    current.next = nxt
                    current = rest
                    tmp.next = rest
                    while nxt.next != current: 
                        nxt = nxt.next
                    nxt.next = rest
                    break
                prev = prev.next
                nxt = nxt.next
            if nxt == current: current = current.next

        return dummy.next

    def printList(self, head): 
        p = head 
        while p: 
            print(p.val, "->", end=" ")
            p = p.next
        print("None")

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l4.next = l2
l2.next = l1
l1.next = l3

sol = Solution()
head = sol.insertionSortList(l4)
sol.printList(head)
