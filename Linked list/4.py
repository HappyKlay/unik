class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return head
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second_half = slow.next
    slow.next = None 
    
    prev = None
    while second_half:
        temp = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = temp
    second_half = prev  
    
    first_half = head
    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next
        first_half.next = second_half
        second_half.next = temp1
        first_half = temp1
        second_half = temp2
    
    return head

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head = reorderList(head)
printList(head) 

# Example 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = reorderList(head)
printList(head)  
