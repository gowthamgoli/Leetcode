from LinkedList import ListNode, listtoListNode, listNodeToList

def removeNthFromEnd(head, n):
    start = ListNode(0)
    slow, fast = start, start
    start.next = head
    for i in range(0, n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return start.next

if __name__ == '__main__':
    head = listtoListNode([1,2,3,4,5,6,7])
    print(listNodeToList(head))
    head = removeNthFromEnd(head, 3)
    print(listNodeToList(head))