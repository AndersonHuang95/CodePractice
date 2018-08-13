# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """

        How can we do this problem iteratively? Intuitively we have to use a stack... 

        We want to pursue nodes in this order: 
        root.left, root, root.right
		
		@2: 
		stack: [2]
		
		@1: 
		curr: 2
		stack: [4, 2]
		ans: [1]
		
		@2: 
		curr: 2
		stack: 


        	2
           / \
          1   4
         / \ / \
        n  n 3	5


        :type root: TreeNode
        :rtype: List[int]
        """

        # if not root: return []
        # left = self.inorderTraversal(root.left) 
        # right = self.inorderTraversal(root.right)
        # return left + [root.val] + right

        if not root: return []
        stack, ans = [], []
        current = root
        while stack or current:
        	while current: 
        		stack.push(current)
        		current = current.next
        	current = stack.pop()
        	ans.append(current.val)
        	current = current.right
