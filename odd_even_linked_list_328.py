from LinkedList import ListNode, listtoListNode, listNodeToList

def oddEvenList(head):
    if head is None: return head

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

if __name__ == '__main__':
    head = listtoListNode([2,1,3,5,6,4,7])
    print(listNodeToList(head))
    head = oddEvenList(head)
    print(listNodeToList(head))