class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0) 
            right = max(dfs(node.right), 0)  
            
            self.max_sum = max(self.max_sum, node.val + left + right)
            
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

solution = Solution()
print(solution.maxPathSum(root1))  # Output: 6

root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

print(solution.maxPathSum(root2))  # Output: 42
