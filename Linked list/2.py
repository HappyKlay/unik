# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head  

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
head = ListNode(1, ListNode(1, ListNode(2)))
head = deleteDuplicates(head)
printList(head)

# Example 2
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
head = deleteDuplicates(head)
printList(head)
