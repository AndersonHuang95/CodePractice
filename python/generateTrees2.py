class TreeNode: 
    def __init__(self, val): 
        self.val = val

def generateTrees(n):
    def node(val, left, right):
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node
    def trees(first, last):
        return [node(root, left, right)
                for root in range(first, last+1)
                for left in trees(first, root-1)
                for right in trees(root+1, last)] or [None]
    return trees(1, n)

print(generateTrees(3))