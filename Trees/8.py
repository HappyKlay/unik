from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode):
        columns = defaultdict(list)
        queue = deque([(root, 0)])  
        
        while queue:
            node, col = queue.popleft()
            
            if node: 
                columns[col].append(node.val) 
                
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
        
        result = [columns[col] for col in sorted(columns.keys())]
        return result

solution = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(solution.verticalTraversal(root1))  # Output: [[9],[3,15],[20],[7]]

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)

print(solution.verticalTraversal(root2))  # Output: [[4],[2],[1,5,6],[3],[7]]

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(6)
root3.right.left = TreeNode(5)
root3.right.right = TreeNode(7)

print(solution.verticalTraversal(root3))  # Output: [[4],[2],[1,5,6],[3],[7]]
