class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    count = 0
    result = None
    
    def inorder(node):
        nonlocal count, result
        
        if not node:
            return
        
        inorder(node.left)
        
        count += 1
        if count == k:
            result = node.val
            return
        
        inorder(node.right)
    
    inorder(root)
    return result

root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(2)
print(kthSmallest(root1, 1))  # Output: 1

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)
print(kthSmallest(root2, 3))  # Output: 3
