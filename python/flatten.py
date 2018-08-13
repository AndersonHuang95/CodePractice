# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        Example: 
            1
           / \
          2   5
         / \   \
        3   4   6

        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6

        We are attempting to do an inorder traversal, all the while flattening the tree into a list. 
        The pseudocode for an-inrder traversal is as follows: 

        inorder(root.left)
        do some work...
        inorder(root.right)

        Therefore, we need to figure out what needs to be done in the code block "do some work..."
        Since this is an in-place solution, writing the tree values out into a new list will not suffice.
        We know that everything in the left subtree extending downward into all the left children will be 
        in correct order already. The problem is attaching the nodes in the right subtree. 

        The problem is slightly ambigious, since the new connections can either be left attached or right attached. 
        Let's approach the problem first by attaching all new nodes to the left, since this seems like
        the easier first-step.

        A solution with O(N) space will traverse the tree in-order and place all nodes in a queue. Then each link 
        to the next node can be made. 

        Args: 
            root (TreeNode): root of tree structure
        
        Returns: 
            void: Modifies tree in place
        """

        # if not root: return 
        # stack, inorder = [root], []
        # while stack: 
        #     current = stack.pop()
        #     inorder.append(current)
        #     if current.right: stack.append(current.right)
        #     if current.left: stack.append(current.left)

        # # --- inorder holds nodes in flattened-list order now ---
        # inorder.append(None)
        # for i in range(len(inorder) - 1): 
        #     inorder[i].left = None
        #     inorder[i].right = inorder[i + 1]

        # --- For an iterative O(1) space solution, we can split into subcases based on left and right subtree existence ---
        while root: 
            # --- if both subtrees exist, we link the greatest node in the left subtree to the root's right subtree
            if root.left and root.right: 
                left = root.left
                while left.right: 
                    left = left.right
                left.right = root.right

            # --- if only the left subtree exists, we move the left subtree into the right subtree, and iterate onto the new right subtree ---
            if root.left: 
                root.right = root.left
            root.left = None
            root = root.right





        