# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """Sorts a linked list using the merge sort algorithm

        The step-by-step process is similar to sorting an array. 
        We divide and conquer. Each time we divide our list in half, and we bottom 
        out until we only have one item in a list. Within the context fo a linked list, 
        we have to check this by checking if the next pointer is None. 

        There is another quirk. When we recurse, we have to make sure to set the first half's
        next to None, so we have a stopping condition for the first half. This is oay isnce
        we will relink pointers in the merge stage.

        The merge stage is identical to merging two sorted linked lists. This invariant holds
        since in our base cases, each list is one element which is by definition sorted

        :type head: ListNode
        :rtype: ListNode
        """

        def merge(first, second): 
            dummy = ListNode(0)
            p = dummy
            while first and second:
                first_val = first.val
                second_val = second.val
                if first_val < second_val: 
                    p.next = first
                    first = first.next
                else: 
                    p.next = second
                    second = second.next
                p = p.next
            if first: p.next = first
            if second: p.next = second
            return dummy.next

        print_list(head)
        # --- base cases: empty or 1-element list ---
        if not head or not head.next: 
            return head

        # --- find middle of list ---
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # --- sever first half of list ---
        tail = slow.next
        slow.next = None
        first = self.sortList(head)
        second = self.sortList(tail)
        return merge(first, second)

l1 = ListNode(1)
l4 = ListNode(4)
l1.next = l4

l2 = ListNode(2)
l3 = ListNode(3)
l2.next = l3

a = ListNode(-1)
b = ListNode(5)
c = ListNode(3)
d = ListNode(4)
e = ListNode(0)
a.next = b
b.next = c
c.next = d
d.next = e

def merge(first, second): 
    dummy = ListNode(0)
    p = dummy
    while first and second:
        first_val = first.val
        second_val = second.val
        if first_val < second_val: 
            p.next = first
            first = first.next
        else: 
            p.next = second
            second = second.next
        p = p.next
    if first: p.next = first
    if second: p.next = second
    return dummy.next

def merge2(first, second): 
    if not first and not second: 
        return None
    if not first: 
        return second
    if not second: 
        return first
    if first.val < second.val: 
        first.next = merge2(first.next, second)
        return first
    else: 
        second.next = merge2(first, second.next)
        return second

def print_list(head):
    while head: 
        print(head.val, "->", end=" ")
        head = head.next
    print("None")

sol = Solution()
ret = sol.sortList(a)
print_list(ret)

