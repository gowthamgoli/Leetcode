from LinkedList import ListNode, listtoListNode, listNodeToList

def reverseList(head):
    start = None
    curr = head
    while curr:
        next = curr.next
        curr.next = start
        start = curr
        curr = next
    return start

def reverseList_rec(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverseList_rec(head.next)
    next_node = head.next
    next_node.next = head
    head.next = None
    return new_head

if __name__ == '__main__':
    head = listtoListNode([1])
    print(listNodeToList(head))
    head = reverseList_rec(head)
    print(listNodeToList(head))