class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def preorder(node):
            if not node:
                return ["null"]
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ",".join(preorder(root))
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        values = data.split(",")
        
        def build_tree():
            val = values.pop(0)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node
        
        return build_tree()

codec = Codec()

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(5)

serialized1 = codec.serialize(root1)
print(serialized1)
deserialized1 = codec.deserialize(serialized1)
print(codec.serialize(deserialized1))

root2 = None
serialized2 = codec.serialize(root2)
print(serialized2)
deserialized2 = codec.deserialize(serialized2)
print(codec.serialize(deserialized2))
