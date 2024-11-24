import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    min_heap = []
    
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, l)
    
    dummy = ListNode()
    current = dummy
    
    while min_heap:
        node = heapq.heappop(min_heap)
        
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(min_heap, node.next)
    
    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
result = mergeKLists(lists)
printList(result) 

# Example 2
lists = []
result = mergeKLists(lists)
printList(result)  

# Example 3
lists = [ListNode()]
result = mergeKLists(lists)
printList(result)  
