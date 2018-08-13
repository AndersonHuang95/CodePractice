# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """Constructor
        
        Initialize the next element to be returned, the leftmost-deep element.
        
        :type root: TreeNode
        """
        self.root = root 
        self._next = []
        while root:
            self._next.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next
        

    def next(self):
        """
        
        Must be called after hasNext() to ensure valid next item exists
        :rtype: int
        """
        ans = self._next.pop()
        if ans.right: 
            curr = ans.right
            while curr: 
                self._next.append(curr)
                curr = curr.left
        return ans.val

def main():
    t1 = TreeNode(1)
    t2 = TreeNode(2) 
    t3 = TreeNode(3)
    t4 = TreeNode(4) 

    t2.left = t1
    t2.right = t4
    t4.left = t3

    ans = []
    it = BSTIterator(t2)
    while it.hasNext():
        ans.append(it.next())

    assert ans == [1, 2, 3, 4]

if __name__ == '__main__':
    main()