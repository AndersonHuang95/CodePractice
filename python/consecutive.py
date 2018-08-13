#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_seq = 1 if root.left and root.left.val == root.val + 1 else 0
        right_seq = 1 if root.right and root.right.val == root.val + 1 else 0
        left_consec = left_seq + self.longestConsecutive(root.left)
        right_consec = right_seq + self.longestConsecutive(root.right)
        return max(left_consec, right_consec)

def main():
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t2 = TreeNode(2)
    t4 = TreeNode(4)
    t5 = TreeNode(5)

    t1.right = t3
    t3.left = t2
    t3.right = t4
    t4.right = t5

    sol = Solution()
    print(sol.longestConsecutive(t1))
    
if __name__ == '__main__':
    main()