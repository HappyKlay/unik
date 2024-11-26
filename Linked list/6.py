class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleNumber(head):
    def reverseList(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    head = reverseList(head)
    
    carry = 0
    current = head
    while current:
        current.val = current.val * 2 + carry
        carry = current.val // 10
        current.val %= 10
        current = current.next
    
    if carry:
        current = ListNode(carry)
        current.next = head
        head = current
    
    head = reverseList(head)
    
    return head

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
head = ListNode(1, ListNode(8, ListNode(9)))
result = doubleNumber(head)
printList(result) 

# Example 2
head = ListNode(9, ListNode(9, ListNode(9)))
result = doubleNumber(head)
printList(result)  
