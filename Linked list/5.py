# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    # Copy the value of the next node to the current node
    node.val = node.next.val
    # Skip the next node
    node.next = node.next.next

# Helper function to print the linked list
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete = head.next  # Node with value 5
deleteNode(node_to_delete)
printList(head)  # Output: 4 -> 1 -> 9 -> None

# Example 2
head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete = head.next.next  # Node with value 1
deleteNode(node_to_delete)
printList(head)  # Output: 4 -> 5 -> 9 -> None
