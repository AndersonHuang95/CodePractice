# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current: 
            if current.val == val:
                after = current.next
                prev.next = after
                del current 
                current = after
            else: 
                prev = prev.next
                current = current.next
        return dummy.next

    def printList(self, head):
        p = head
        while p: 
            print(p.val, "->", end=' ')
            p = p.next


def main():
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(6)
    l5 = ListNode(4)
    l6 = ListNode(5)
    l7 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7

    sol = Solution()
    sol.printList(l1)
    print()
    head = sol.removeElements(l1, 6)
    sol.printList(head)

if __name__ == '__main__':
    main()