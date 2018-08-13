# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# 
# Return c1

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """Finds the intersection node of two lists, guaranteed the lists have no cycle

        A simple solution using memory proportional to both lists is to create two sets
        which hold the nodes for each list. We then find the intersection of the two sets
        by going stepwise through the sets. This is all good, but can we do better
        and do the operation in constant memory? 

        The other option would be to treat each list like an array, and we step through
        both until we see a match. Wil this result in any inconsistencies? 
        Unfortunately yes, because we don't know when to move which pointer. We don't
        have enough information! 

        Perhaps the length of the lists will help us? We can preprocess both lists
        and get the length of both. 

        A piece of information we have neglected so far is that the lists must
        become the same list eventually. Meaning, they share X amount of nodes.
        Now we have the conditional to determine when to move each pointer.
        When A is ahead of B, we move B, and vice versa. Eventually, the lengths
        must intersect.

        A:          a1 → a2
                            ↘
                              c1 → c2 → c3
                            ↗            
        B:     b1 → b2 → b3

        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # --- Handle empty lists --- 
        length_A = 0
        a = headA
        while a: 
            a = a.next
            length_A += 1

        length_B = 0 
        b = headB
        while b: 
            b = b.next
            length_B += 1

        # --- let A be the longer list ---
        if length_A < length_B:
            headA, headB = headB, headA

        diff = abs(length_A - length_B)

        a, b = headA, headB
        while diff: 
            a = a.next
            diff -= 1

        while a and b: 
            if a == b: return a
            a, b = a.next, b.next

        # --- No intersection found ---
        return None

def main():
    # --- driver program ---
    sol = Solution()

    # test empty lists
    assert sol.getIntersectionNode(None, None) == None

    # test one empty list 
    l1 = ListNode(0)
    assert sol.getIntersectionNode(l1, None) == None

    # test two valid lists
    a1, a2 = ListNode(0), ListNode(0)
    b1, b2, b3 = ListNode(0), ListNode(0), ListNode(0)
    c1, c2, c3 = ListNode(0), ListNode(0), ListNode(0)

    a1.next = a2
    a2.next = c1
    b1.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2.next
    c2.next = c3.next 

    assert sol.getIntersectionNode(a1, b1) == c1

if __name__ == '__main__':
    main()
        