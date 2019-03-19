from LinkedList import ListNode, listtoListNode, listNodeToList
def mergeTwoLists(l1, l2):
    dummy_root = ListNode(0)
    ptr = dummy_root
    while l1 and l2:
        if l1.val <= l2.val:
            ptr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            ptr.next = ListNode(l2.val)
            l2 = l2.next
        ptr = ptr.next
    if l1:
        ptr.next = l1
    if l2:
        ptr.next = l2    
    return dummy_root.next

if __name__ == '__main__':
    l1 = listtoListNode([1, 2, 4])
    l2 = listtoListNode([1, 2, 5, 6, 7])
    head = mergeTwoLists(l1, l2)
    print(listNodeToList(head))