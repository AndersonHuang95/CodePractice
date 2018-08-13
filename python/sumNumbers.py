# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        Example: 

            1
           / \
          2   3

        Output: 25

        We need to aggregate all sums. We can pass a list to keep
        track of the running sum, or we can store all results, 
        and then sum after we finish traversing all root-to-leaf paths

        In the worst case, our tree is unbalanced and looks like a straight line.
        So we have to recurse through all n nodes, meaning we use up O(N) space. 
        We also use O(N) space for the intermeidate list (but we could also not use
        the list, it's a little bit nicer looking since python doesn't allow modification
        of primitives). Finally, the algorithm is O(n) since we must go thru all nodes. 

        :type root: TreeNode
        :rtype: int
        """

        def recurse(root, total):
            if not root: return 0
            if not root.left and not root.right: return total * 10 + root.val
            return recurse(root.left, total * 10 + root.val) + recurse(root.right, total * 10 + root.val)
        return recurse(root, 0)


    def sumNumbersIterative(self, root):
        if not root: return 0 
        total = 0
        stack = [root]
        while stack:
            current = stack.pop()
            if not current.left and not current.right: 
                total += current.val 
            if current.left:
                tmp = current.lefts
                tmp.val += current.val * 10
                stack.append(tmp)
            if current.right:
                tmp = current.right
                tmp.val += current.val * 10
                stack.append(tmp)
        return total

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
sol = Solution()
print(sol.sumNumbers(t1))
print(sol.sumNumbersIterative(t1))