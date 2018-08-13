# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """

        Example:

        Input: 3
        Output:
        [
          [1,null,3,2],
          [3,2,null,1],
          [3,1,null,null,2],
          [2,1,3],
          [1,null,2,null,3]
        ]
        Explanation:
        The above output corresponds to the 5 unique BST's shown below:

           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3
        :type n: int
        :rtype: List[TreeNode]

        To solve this problem, we must fundamentally understand what binary search trees are.

        Binary search trees are data structures that order its items. Everything in the left subtree
        is less than the current node, and everything in the right subtree is greater than the current node.

        Let's try the example with n = 3

        list[1 2 3]    Try with 1 as root, okay because cand is empty
             ^

            list[1 2 3]        Try with 2 as left? not possible, Try with 2 as right? okay
                   ^
            cand[1]

                list[1 2 3]        Try with 3 as left? not possible, Try 3 with right? okay
                         ^
                cand[1 null 2]

                    list[1 2 3]
                                ^
                    cand[1 null 2 3]    out of nums, add to ans

            list[1 3 2]        Try with 3 as right
                   ^
            cand[1]

                list[1 2 3]
        """
        nums = [x for x in range(1, n + 1)]
        ans, cand = [], []
        self.backtrack(nums, ans, cand, 0, n)
        return ans

    def backtrack(self, nums, ans, cand, left, right):
        if left >= right: 
            return nums[left]
        for i in range(left, right):
            cand = self.backtrack(nums, ans, cand + [nums[i]], left, i - 1)
            + self.backtrack(nums, ans, cand + [nums[i]], i + 1, right)
            # --- Try as root ---
            if idx == 0:
                self.backtrack(nums, ans, cand + [nums[idx]], idx + 1)
            # --- Try as left child of previous ---
            elif nums[idx] < cand[-1]:
                self.backtrack(nums, ans, cand + [nums[idx]], idx + 1)
            # --- Try as right child of previous ---
            else:
                self.backtrack(nums, ans, cand + [None] + [nums[idx]], idx + 1)
            nums[i], nums[idx] = nums[idx], nums[i]

sol = Solution()
print(sol.generateTrees(3))
