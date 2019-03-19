from LinkedList import *

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    head = listtoListNode([3])
    # second = head.next
    # head.next = head
    # last.next = second/
    # print(listNodeToList(head))
    print(hasCycle(head))