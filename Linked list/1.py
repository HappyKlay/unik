# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    prehead = ListNode(-1)
    prev = prehead
    
    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next
    
    prev.next = list1 if list1 else list2
    
    return prehead.next  

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = mergeTwoLists(list1, list2)
printList(merged_list)

# Example 2
list1 = None
list2 = None
merged_list = mergeTwoLists(list1, list2)
printList(merged_list)

# Example 3
list1 = None
list2 = ListNode(0)
merged_list = mergeTwoLists(list1, list2)
printList(merged_list)

