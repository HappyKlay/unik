class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(S: str) -> TreeNode:
    stack = []
    i = 0
    
    while i < len(S):
        depth = 0
        while i < len(S) and S[i] == '-':
            depth += 1
            i += 1
        
        value = 0
        while i < len(S) and S[i].isdigit():
            value = value * 10 + int(S[i])
            i += 1
        
        node = TreeNode(value)
        
        if depth == len(stack):
            if stack:
                stack[-1].left = node
        else:
            while len(stack) > depth:
                stack.pop()
            if stack:
                stack[-1].right = node
        
        stack.append(node)
    
    return stack[0]
    
from collections import deque

def print_tree(root):
    if not root:
        return "[]"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    
    while result and result[-1] == "null":
        result.pop()
    
    return str(result)

S = "1-2--3--4-5--6--7"
root = recoverFromPreorder(S)
print(print_tree(root))  # Output: [1, 2, 5, 3, 4, 6, 7]

S = "1-2--3---4-5--6--7"
root = recoverFromPreorder(S)
print(print_tree(root))  # Output: [1, 2, 5, 3, null, 6, null, 4, null, 7]

S = "1-401--349---90--88"
root = recoverFromPreorder(S)
print(print_tree(root))  # Output: [1, 401, null, 349, 88, 90]
