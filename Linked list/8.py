class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverse_linked_list(start, end):
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    node_count = 0
    node = head
    while node:
        node_count += 1
        node = node.next
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy  
    
    while node_count >= k:
        group_start = group_prev.next  
        group_end = group_start
        for _ in range(k - 1):
            group_end = group_end.next
        next_group_start = group_end.next
        group_end.next = None  # Temporarily terminate the group
        reversed_head = reverse_linked_list(group_start, None)
        group_prev.next = reversed_head
        group_start.next = next_group_start
        group_prev = group_start
        node_count -= k
    
    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k1 = 2
result1 = reverseKGroup(head1, k1)
printList(result1) 

# Example 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k2 = 3
result2 = reverseKGroup(head2, k2)
printList(result2)  
