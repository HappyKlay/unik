class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head

    dummy = ListNode(-1)
    dummy.next = head
    prev, current = dummy, head

    while current and current.next:
        first, second = current, current.next
        prev.next, first.next, second.next = second, second.next, first
        prev, current = first, first.next
    
    return dummy.next

def list_to_linkedlist(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example 1
head = list_to_linkedlist([1, 2, 3, 4])
print(linkedlist_to_list(swapPairs(head)))  

# Example 2
head = list_to_linkedlist([])
print(linkedlist_to_list(swapPairs(head)))  

# Example 3
head = list_to_linkedlist([1])
print(linkedlist_to_list(swapPairs(head)))  
