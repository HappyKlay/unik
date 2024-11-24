class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 2 

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.cameras += 1
                return 1  

            if left == 1 or right == 1:
                return 2 

            return 0  

        self.cameras = 0
        
        if dfs(root) == 0:  
            self.cameras += 1
        
        return self.cameras

solution = Solution()

root1 = TreeNode(0)
root1.left = TreeNode(0)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(0)

print(solution.minCameraCover(root1))  # Output: 1

root2 = TreeNode(0)
root2.left = TreeNode(0)
root2.left.left = TreeNode(0)
root2.right = TreeNode(0)
root2.right.right = TreeNode(0)

print(solution.minCameraCover(root2))  # Output: 2
