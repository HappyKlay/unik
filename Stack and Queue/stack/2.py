class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    def traverse(node):
        if node is None:
            return []
        return traverse(node.left) + [node.val] + traverse(node.right)
    
    return traverse(root)

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversal(root1))  # Output: [1, 3, 2]

root2 = None
print(inorderTraversal(root2))  # Output: []

root3 = TreeNode(1)
print(inorderTraversal(root3))  # Output: [1]
