# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        We can do this iteratively. Since k may be greater than the length of the list, 
        we can prevent unneccessary rotations by first doing modulo arithmetic on k by the
        length of the list. Then we break the list into two pieces, where the second piece
        is of length k. We attach this piece to the first piece which is of length (n - k).
        And then we make sure to set the end of the first piece to be None. 

        Special cases are a big area of concern for linked lists. We make sure not to do unnecessary 
        work or deference null values by not doing any action when k % len(list) == 0.

        Special care must also be taken for length 0 and length 1 lists since rotation are no-ops
        for lists of these types. Therefore, for the three aforementioned scenarios, we simply
        return the list as is. 

        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr, length = head, 0
        while curr: 
        	length += 1
        	curr = curr.next

        if k == 0 or length <= 1 or (k % length) == 0: return head

        k %= length
        # we want to stop right before the second half of the list
        curr, first_length = head, length - k - 1
        while first_length: 
        	first_length -= 1
        	curr = curr.next
        new_head, curr.next = curr.next, None

        # now relink the end of the second piece to the first
        curr = new_head
        while curr.next: 
        	curr = curr.next
        curr.next = head

        return new_head





