class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitList(head, x):
    less_head = ListNode(0)
    greater_head = ListNode(0)
    
    less = less_head
    greater = greater_head
    
    current = head
    while current:
        if current.val < x:
            less.next = current 
            less = less.next
        else:
            greater.next = current  
            greater = greater.next
        current = current.next
    greater.next = None
    less.next = greater_head.next
    return less_head.next

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
head1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))) 
x1 = 3
result1 = splitList(head1, x1)
printList(result1) 

# Example 2
head2 = ListNode(2, ListNode(1))
x2 = 2
result2 = splitList(head2, x2)
printList(result2) 
