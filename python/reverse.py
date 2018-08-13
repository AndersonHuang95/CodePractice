#/usr/bin/env python3

class ListNode: 
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    before, current = None, head
    while current:
        after = current.next
        current.next = before
        before = current
        current = after
    return before

l1 = ListNode(1)