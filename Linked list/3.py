class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next            
        fast = fast.next.next       
        
        if slow == fast:          
            return True
    
    return False 

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next 

print(hasCycle(head))  

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head  

print(hasCycle(head))  

head = ListNode(1)
print(hasCycle(head))  
